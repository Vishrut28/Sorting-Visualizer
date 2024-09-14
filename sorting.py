import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Visualizer")

# Colors
BACKGROUND = (25, 25, 25)
BAR_COLOR = (100, 180, 255)
COMPARE_COLOR = (255, 150, 150)
SWAP_COLOR = (150, 255, 150)
TEXT_COLOR = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

# Generate random array
array_size = 100
array = [random.randint(10, height - 60) for _ in range(array_size)]

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_array(arr, j, j + 1)
                pygame.time.delay(5)

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        draw_array(arr, k - 1)
        pygame.time.delay(5)
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        draw_array(arr, k - 1)
        pygame.time.delay(5)
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
        draw_array(arr, k - 1)
        pygame.time.delay(5)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, i, j)
            pygame.time.delay(5)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_array(arr, i + 1, high)
    pygame.time.delay(5)
    return i + 1

# Function to draw the array as rectangles
def draw_array(arr, current_index=None, swap_index=None):
    screen.fill(BACKGROUND)
    bar_width = (width - 100) // len(arr)
    for i, height in enumerate(arr):
        color = BAR_COLOR
        if i == current_index:
            color = COMPARE_COLOR
        if i == swap_index:
            color = SWAP_COLOR
        pygame.draw.rect(screen, color, (50 + i * bar_width, height + 50, bar_width - 1, height))

    # Draw title
    title = title_font.render("Sorting Visualizer", True, TEXT_COLOR)
    screen.blit(title, (width // 2 - title.get_width() // 2, 10))

    # Draw instructions
    instructions = [
        "R: Reset",
        "B: Bubble Sort",
        "M: Merge Sort",
        "Q: Quick Sort"
    ]
    for i, instruction in enumerate(instructions):
        text = font.render(instruction, True, TEXT_COLOR)
        screen.blit(text, (10, height - 120 + i * 30))

    pygame.display.flip()

# Main game loop
running = True
sorting = False
sort_algorithm = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                array = [random.randint(10, height - 60) for _ in range(array_size)]
            elif event.key == pygame.K_b and not sorting:
                sorting = True
                sort_algorithm = bubble_sort
            elif event.key == pygame.K_m and not sorting:
                sorting = True
                sort_algorithm = lambda arr: merge_sort(arr, 0, len(arr) - 1)
            elif event.key == pygame.K_q and not sorting:
                sorting = True
                sort_algorithm = lambda arr: quick_sort(arr, 0, len(arr) - 1)

    if sorting:
        sort_algorithm(array)
        sorting = False

    draw_array(array)

pygame.quit()
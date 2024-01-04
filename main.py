from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Sudoku import *

def fillBoard(driver):
    board = [[0 for i in range(9)] for j in range(9)]

    prefilledValues = driver.find_elements(By.XPATH, "//div[contains(@role, 'grid')]//div[contains(@class, 'su-cell selected prefill') or (contains(@class, 'su-cell prefilled')) and not(contains(@aria-label, 'empty'))]")
    for element in prefilledValues:
        CellNumber = element.get_attribute('data-cell')
        CellValue = int(element.get_attribute('aria-label'))

        column = int(CellNumber) % 9
        row = int(CellNumber) // 9
        #print("Row: ", row, " | Column: ", column, "| CellNumber: ", CellNumber, " | Value: ", CellValue)
        
        board[row][column] = CellValue
    
    return board

def placeValueInCell(driver, cellID, cellValue):
    cell_xpath = f"//div[contains(@role, 'grid')]//div[contains(@data-cell, '{str(cellID)}')]"
    cell_element = driver.find_element(By.XPATH, cell_xpath)
    driver.execute_script(f"arguments[0].value = '{str(cellValue)}';", cell_element)
    actions = ActionChains(driver)
    actions.click(cell_element).perform()

def placeSolution(driver, solved_board):
    for i in range(9):
        for j in range(9):
            cell_id = i * 9 + j 
            cell_value = solved_board[i][j]
            placeValueInCell(driver, cell_id, cell_value)
            time.sleep(0.1)  

def main():
    # dynamically install correct version, if downloaded already, load using cache
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    # alternative:
    # DRIVER_PATH = '/path/to/chromedriver'
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)


    difficulty = input("nytimes Sudoku Solver: Choose difficulty (easy,medium,hard)").lower()

    while (difficulty not in [ "easy", "medium", "hard"]):
        difficulty = input("NYtimes Sudoku Solver: Choose difficulty (easy,medium,hard)").lower()

    

    


    try:
        print("Navigating to the Sudoku puzzle...")
        puzzle_url = f"https://www.nytimes.com/puzzles/sudoku/{difficulty}"
        driver.get(puzzle_url)

        print("Filling initial board...")
        sudoku_board = fillBoard(driver)
        printBoard(sudoku_board)

        print("Solving Sudoku...")
        solveBoard(sudoku_board)
        printBoard(sudoku_board)

        input("Press Enter to end.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

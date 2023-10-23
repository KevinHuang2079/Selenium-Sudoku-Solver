from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from Sudoku import *

def fillBoard(driver):
    board = [[0 for i in range(9)] for j in range(9)]

    prefilledValues = driver.find_elements(By.XPATH, "//div[contains(@role, 'grid')]//div[contains(@class, 'su-cell selected prefill') or (contains(@class, 'su-cell prefilled')) and not(contains(@aria-label, 'empty'))]")
    
    # print("Element amount:",  len(prefilledValues))
    # for element in prefilledValues:
    #     print(element.get_attribute('aria-label'))

    for element in prefilledValues:
        CellNumber = element.get_attribute('data-cell')
        CellValue = element.get_attribute('aria-label')

        column = int(CellNumber) % 9
        row = int(CellNumber) // 9
        #print("Row: ", row, " | Column: ", column, "| CellNumber: ", CellNumber, " | Value: ", CellValue)
        
        board[row][column] = CellValue
    
    return board


def main():
    #dynamically install correct version, if downloaded already, load using cache
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    #alternative:   
        #DRIVER_PATH = '/path/to/chromedriver'
        #driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    driver.get("https://www.nytimes.com/puzzles/sudoku/easy")
    sudoku_board = fillBoard(driver)

    driver.quit()

    print("Sudoku Board:")
    printBoard(sudoku_board)

    print("---------------------")
    print("Solved Board:")

    solveBoard(sudoku_board)
    printBoard(sudoku_board)

if __name__ == "__main__":
    main()
<h1 align="center">
  <br>
  <img src="https://www.kindpng.com/picc/m/74-744558_cash-money-clip-art-coupon-vector-material-transparent.png" alt="Markdownify" width="200"></a>
  <br>
  ATM Simulation V1
  <br>
</h1>

<p align="center">
    Matthew Ng 2023©
</p>

## What is this?
This script simulates using an ATM machine for basic note exchanging. You will be asked how many of each note denomination you want to deposit, then will be asked which notes you want in return based on the total value deposited.

## How it works
This program has been tested in Python IDLE and VSCode.
1. In the first stage you will be asked how many of each note denomination you want to recieve. The script will start at 5's and works it's way up to 100's. Enter the appropriate values.

2. Now you will be asked to deposit notes to meet the required balance. Only valid note denominations are allowed as the input (5, 10, 20, 50, 100). Continue this until the remaining balance hits zero**.

**If the the user deposit exceeds the required amount then the script will stop because the "Transaction cannot be completed"

## Example
<img src="https://i.imgur.com/ZKN4Thf.png">

## Important
The beginning of the script would be cleaner if a dictionary and a for loop were to be used. This may be added in newer versions.

The script is based on Australian note denominations.

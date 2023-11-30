# adventofcode2023
Repo for AoC 2023

Yo, back at it, but not really certain how far I'm going to be getting "through" it this year.

Entire repo will be in Python.  I'm going to try my hand at using some actions/automation this year to test my code in github against data hosted privately in S3 since Topaz does not want the AoC puzzle inputs publicly hosted.

Basic mechanics of setting up a day:
* Each solution has it's own Day#.py file
* The Update_Input.py file is used to push the days input to the private S3 located JSON file.
* Each Day#.py will have it's own test cases from the problem and problem URL in the solution.
* A global flag is present for the purpose of switching between test cases and puzzle input.
* Part 1 and Part 2 exist in the same file and will be wholly independent solutions even if redundant code exists in the same solution file.

Happy Honda-days and a merry Toyotathon to all.

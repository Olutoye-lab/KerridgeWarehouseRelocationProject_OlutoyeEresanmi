# KerridgeWarehouseRelocationProject_OlutoyeEresanmi


This project is based around project 5 for the KCS x NUCATS hackathon

The project involves using AI to plan a warehouse relocation project. planned to move items from a base 
in sheffield to a base in Newcastle

Given a number of trucks with a set volume (length x width x height) and a maximum capacity, the goal is to pack these
trucks with a set number of items, such that, the relocation takes the shortest time possible.

## Project layout
There are two parts to this project: 
1. Sorting algorithm
2. Visualisation script


### Sorting algorithm

In order to move items in the shortest time possible, each truck must be packed with the optimum 
arrangement of items, while meeting the constraints of weight, shape and size.

- This problem is synonymous to a 3d bin packing problem, a notorious NP-hard problem 
(Non-deterministic Polynomial time), which is part of a class of the hardest problems in computational complexity.

As this problem's difficulty lied in finding an optimum solution. 
The method used to find an approximate solution was Linear Programming.

But because of this, simulating real and accurate placements of these items was impossible given the time constraints.

As a result, as opposed to considering both shape and size, the overall volume of the shape was considered to resolve 
to a mathematically optimum solution.

- Note: Due to the large number of items in the data files, the solver runs by considering items in cases (100 items per case).

### Visualisation script
This script visualises how a solution to the problem would work.

It uses a manim and mathematical visuals library. 

A Video should be in the Media Directory displaying this information. If not it should have been 
submitted alongside the project

- The library uses a ffmpeg video format, which requires a ffmpeg file to be placed into the C directory of the local machine
these can do downloaded here: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip: (For Windows)
- Extract the files
- Place the bin folder into the C directory
- Restart the Program

In order to run, copy and paste -- "manim -pql BoxRepr.py SolutionSample" into the terminal

### Discalmer:

During production, it was realised that certain items have a volume larger than the volume of the truck, which made 
it difficult to devise an appropriate solution. As a result the items are filtered before being used, with items being 
removed if they had a volume larger than 1/3 of the truck's volume. 

Because of this, An indicator of the number of items being sorted into boxes is clearly indicated in each case.

### Notes:

The in the Main directory, files are:
- Data dir - Contains all the data files used in the project (.json format)
- Media dir - Contains visualisations in the expected outcome of a truck being filled by an algorithm
- BoxRepr.py - Contains the script for the visualising a truck.
- LpProblem.py - Contains the main algorithm
- LpResult.py - Contains the script to show results of the main algorithm

### To run
When running the LpResult.py file, the placements of items is shown via the terminal, along with the case number, 
number of items considered in each case, as well as each which items are packed into which truck.

To run the main algorithm.
- Change directory to MainDir -- 
"cd MainDir"
- Copy and paste into terminal -- 
"python LpResult.py data_100_items.json"

Other data files can be chosen (except BoxTestData.json)
- Example (python LpResult.py data_1000_items.json)
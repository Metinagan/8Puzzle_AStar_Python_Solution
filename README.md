# 8-Puzzle_A-_Python_Solution

<p align="left"> <img src="https://komarev.com/ghpvc/?username=metinagan&label=Profile%20views&color=0e75b6&style=flat" alt="metinagan" /> </p>


#initial matrix

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/1b1cbbbe-8d5d-469c-a3b2-33111a7065ee">



#end matrix

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/147aa8f5-e1dd-4591-a963-08b3d0cda1bf">




#Hamming value calculation

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/a2730497-02af-423e-8d8d-bb179ed10980">




#Mannathen value calculation.

#distance of the indexes of the current matrix to where they should be in the ending matrix.

#Subtraction must be done with absolute value.

#Because: If the element that should be at position [2][2] is at position [0][0], the distance gives a negative result.

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/6edffcf5-a965-44f8-b5f4-381cfd09edd4">





#Heuristic value is the sum of mannathen and hamming values.

#heuristic value intuitively represents our distance from the outcome.

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/1cf17203-a8c5-4769-8a31-202f036f6ada">



#Returns the row and column containing element 0 in the matrix

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/d98ce870-4211-40ab-9d81-4a3e3603e6af">




#Adds to the list the places where the number 0 can move within the matrix

#clears the list before each step

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/8d72cb11-4deb-45f8-9c28-4cde1c0a5a70">



#The function requires a matrix, row and column as values.

#If newly created matrices already exist, we do not add them to the list.

#This way we don't go through the same step again.

#and the function does not stay in an infinite loop

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/562c5044-88aa-429b-875a-70c2234840a9">



#We print the matrix.

#We give 2 seconds of sleep time. Because the matrixs flow so fast.

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/3c193124-94cb-4668-ad7a-18311e697c6f">


    
#Sıfır sayısının gidebileceği yere sıfır sayısını alıyoruz.

#Adds the new matrices we created to the list.

#This function creates matrices which will be one of our next steps.

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/04cf66c8-ebff-4282-b2f1-dce79a3a9587">




#A-Star Algorithm

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/14fb72ae-9f5a-4606-aea8-9122242acc3d">



#Clear main list and add starting matrix to the end of the list

#Finally send the last element of the main list to the function

<img src="https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/1dce3597-57a4-4164-9d54-efbe9bd4b863">














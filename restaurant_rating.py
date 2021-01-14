#enter -1 to give rating and end
print("Rate this restaurant on a scale of 1-5")

poor = 0
mediocre = 0
average = 0
good = 0
excellent = 0
ratings_count = 0
while True:
   
    rating = int(input("1. Poor, 2. Mediocre, 3. Average, 4. Good, 5. Excellent: "))
    if rating == 1:
        poor +=1
    if rating == 2:
        mediocre +=1
    if rating == 3:
        average +=1
    if rating == 4:
        good +=1
    if rating == 5:
        excellent +=1
    if rating == -1:
        print("{:<30}{:>20}".format("poor rating count", poor))
        print("{:<30}{:>20}".format("mediocre rating count", mediocre))
        print("{:<30}{:>20}".format("average rating count", average))
        print("{:<30}{:>20}".format("good rating count", good))
        print("{:<30}{:>20}".format("excellent rating count", excellent))
        poor_t = poor * 1
        mediocre_t = mediocre * 2
        average_t = average * 3
        good_t = good * 4
        excellent_t = excellent * 5

        total_ratings = poor_t + mediocre_t + average_t + good_t + excellent_t
        average_r = total_ratings / ratings_count
        average_ratings_word = "Rating"
        if average_r < 1.5:
            average_ratings_word = "Poor"
        if 1.4 < average_r < 2.5:
            average_ratings_word = "mediocre"
        if 2.4 < average_r < 3.5:
            average_ratings_word = "average"
        if 3.4 < average_r < 4.5:
            average_ratings_word = "good"
        if average_r > 4.4:
            average_ratings_word = "excellent"




        print("{:<25}{:>20}{:^10}{:<10}".format("The average of all the ratings is: ", average_r, "-", average_ratings_word))
        
        break
    ratings_count +=1

        
    
        
        






#result of mathches
results = ['win', 'lost', 'lost', 'win', 'lost'] 

#points given for players per match
player_points = [
    [27, 20, 10],
    [22, 10, 5],
    [20, 10, 30],
    [20, 30, 20],
    [10, 5, 2]
]

def calculate_team_performance(results):
    count_w = 0
    count_l = 0
    len_results = len(results)
    
    for result in results:
        if result == 'win':
            count_w +=1
        if result == 'lost':
            count_l +=1
    team_perfomance = count_w / len_results 
    #add 10% bonus if overall wins are more than 50%
    if (len_results // 2) < count_w:
        return (team_perfomance + team_perfomance * 0.1)
    else:
        return team_perfomance

def player_performance(points):
    total_points = sum(points)
    total_matches = len(points)
    total_avg = total_points / total_matches
    
#more than 30% == bonus = +10 points
    if any(point > 30 for point in points):
        total_avg +=5
    return total_avg

def final_report(results, player_avg_points):
    team_perfomance = calculate_team_performance(results)
    tot_avg_points = sum(player_avg_points) / len(player_avg_points)
    
    totally = (team_perfomance * tot_avg_points) // 2

    if totally > 0.8:
        print("Great work")
    else:
        print("Need to work on something")

player_avg_points = [player_performance(points) for points in player_points]

final_report(results, player_avg_points)

#if it would be NON-KISS:
# Calculate average scores for all players using a for loop
# player_avg_points = []  # Create an empty list to store results
# for points in player_points:
#     avg = player_performance(points)  # Calculate the average for each player
#     player_avg_points.append(avg)     # Add the result to the list

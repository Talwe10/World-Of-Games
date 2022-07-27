import os


def add_score(difficulty):  # put the full path of Scores.txt in a variable:
    path_folder = os.path.dirname(__file__)  # the path of the folder, where the file is
    rel_path = "Scores.txt"

    abs_file_path = os.path.join(path_folder, rel_path)  # abs_file_path = path_folder +'/Scores.txt'
    points_of_winning = ((difficulty * 3) + 5)

    # print("those are the points_of_winning :", points_of_winning)  # checking point

    # open the file to read it, then close it
    with open(abs_file_path, 'r') as f:
        data = f.read()
        score_in_file = int(data)

        # add the current score in file to var: points_of_winning
        points_of_winning = points_of_winning + score_in_file
        f.close()

    # open the file again to write the score, then close it
    with open(abs_file_path, 'w') as f:
        f.write(str(points_of_winning))

import csv
import sys 
import os 

current_dir = os.path.dirname(__file__)
election_data_path = os.path.join(current_dir, './Resources/election_data.csv')

total_votes = 0
candidates = {}
winner = {'name': '', 'votes': 0}


with open(election_data_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)



    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        candidates[candidate] = {'percentage': percentage, 'votes': votes}

    for candidate, data in candidates.items():
        if data['votes'] > winner['votes']:
            winner['name'] = candidate
            winner['votes'] = data['votes']

    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')

    for candidate, data in candidates.items():
        print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
    print('-------------------------')

    print(f"Winner: {winner['name']}")
    print('-------------------------')



import json
import os
import numpy as np
from functions import *


t20_dir = 't20_m/'

list_of_files = [file for file in os.listdir(t20_dir) if file.endswith(".json")]

sorted_list = sorted(list_of_files, key=extract_number)



# Winner 0 = batting first win, 1 = batting second win

def get_t20_details(year):
    t20_matches_details = np.array([], dtype=[('target', 'i4'), ('first_inn_q1_runs', 'i4'), ('first_inn_q2_runs', 'i4'), ('first_inn_q3_runs', 'i4'), ('first_inn_q4_runs', 'i4'), ('second_inn_q1_runs', 'i4'), ('second_inn_q2_runs', 'i4'), ('second_inn_q3_runs', 'i4'), ('second_inn_q4_runs', 'i4'), ('first_inn_q1_wickets', 'i4'), ('first_inn_q2_wickets', 'i4'), ('first_inn_q3_wickets', 'i4'), ('first_inn_q4_wickets', 'i4'), ('second_inn_q1_wickets', 'i4'), ('second_inn_q2_wickets', 'i4'), ('second_inn_q3_wickets', 'i4'), ('second_inn_q4_wickets', 'i4'), ('first_inn_q1_deliveries', 'i4'), ('second_inn_q1_deliveries', 'i4'), ('first_inn_q2_deliveries', 'i4'), ('second_inn_q2_deliveries', 'i4'), ('first_inn_q3_deliveries', 'i4'), ('second_inn_q3_deliveries', 'i4'), ('first_inn_q4_deliveries', 'i4'), ('second_inn_q4_deliveries', 'i4'), ('winner', 'i4')])
    try: 
        for filename in sorted_list:
            with open(t20_dir + filename, 'r') as f:
                data = json.load(f)
                match_date = data['info']['dates'][0]
                match_date = match_date.split('-')
                if ('by' in data['info']['outcome']):
                    if (int(match_date[0]) > year):
                        target_overs =  data['info']['overs']
                        if 'runs' in data['info']['outcome']['by']:
                            winner = 0
                        else:
                            winner = 1
                        
                        if (target_overs == 20):
                            first_inn_q1_deliveries = 0
                            second_inn_q1_deliveries = 0
                            first_inn_q2_deliveries = 0
                            second_inn_q2_deliveries = 0
                            first_inn_q3_deliveries = 0
                            second_inn_q3_deliveries = 0
                            first_inn_q4_deliveries = 0
                            second_inn_q4_deliveries = 0
                            first_inn_q1_runs = 0
                            first_inn_q1_wickets = 0
                            first_inn_q2_runs = 0
                            first_inn_q2_wickets = 0
                            first_inn_q3_runs = 0
                            first_inn_q3_wickets = 0
                            first_inn_q4_runs = 0
                            first_inn_q4_wickets = 0
                            second_inn_q1_runs = 0
                            second_inn_q1_wickets = 0
                            second_inn_q2_runs = 0
                            second_inn_q2_wickets = 0
                            second_inn_q3_runs = 0
                            second_inn_q3_wickets = 0
                            second_inn_q4_runs = 0
                            second_inn_q4_wickets = 0

                            match_inning = 1
                            for inning in data['innings']:
                                if match_inning == 1:
                                    for over in inning['overs']:
                                        if 0 <= over['over'] < 5:
                                            for delivery in over['deliveries']:
                                                first_inn_q1_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    first_inn_q1_wickets += 1
                                                first_inn_q1_deliveries += 1
                                        
                                        elif 5 <= over['over'] < 10:
                                            for delivery in over['deliveries']:
                                                first_inn_q2_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    first_inn_q2_wickets += 1
                                                first_inn_q2_deliveries += 1
                                        
                                        elif 10 <= over['over'] < 15:
                                            for delivery in over['deliveries']:
                                                first_inn_q3_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    first_inn_q3_wickets += 1
                                                first_inn_q3_deliveries += 1
                                        
                                        elif 15 <= over['over'] < 20:
                                            for delivery in over['deliveries']:
                                                first_inn_q4_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    first_inn_q4_wickets += 1
                                                first_inn_q4_deliveries += 1
                                        
                                
                                if match_inning == 2:
                                    for over in inning['overs']:
                                        if 0 <= over['over'] < 5:
                                            for delivery in over['deliveries']:
                                                second_inn_q1_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    second_inn_q1_wickets += 1
                                                second_inn_q1_deliveries += 1

                                        elif 5 <= over['over'] < 10:
                                            for delivery in over['deliveries']:
                                                second_inn_q2_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    second_inn_q2_wickets += 1
                                                second_inn_q2_deliveries += 1
                                        
                                        elif 10 <= over['over'] < 15:
                                            for delivery in over['deliveries']:
                                                second_inn_q3_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    second_inn_q3_wickets += 1
                                                second_inn_q3_deliveries += 1
                                        
                                        elif 15 <= over['over'] < 20:
                                            for delivery in over['deliveries']:
                                                second_inn_q4_runs += delivery['runs']['total']
                                                if ('wickets' in delivery):
                                                    second_inn_q4_wickets += 1
                                                second_inn_q4_deliveries += 1
                                        
                                match_inning += 1


                            target = sum(first_inn_q1_runs, first_inn_q2_runs, first_inn_q3_runs, first_inn_q4_runs)
                            t20_matches_details = np.append(t20_matches_details, np.array([(target, first_inn_q1_runs, first_inn_q2_runs, first_inn_q3_runs, first_inn_q4_runs, second_inn_q1_runs, second_inn_q2_runs, second_inn_q3_runs, second_inn_q4_runs, first_inn_q1_wickets, first_inn_q2_wickets, first_inn_q3_wickets, first_inn_q4_wickets, second_inn_q1_wickets, second_inn_q2_wickets, second_inn_q3_wickets, second_inn_q4_wickets, first_inn_q1_deliveries, second_inn_q1_deliveries, first_inn_q2_deliveries, second_inn_q2_deliveries, first_inn_q3_deliveries, second_inn_q3_deliveries, first_inn_q4_deliveries, second_inn_q4_deliveries, winner)], dtype=t20_matches_details.dtype))

                            # print('----------------------------------------\n')
        return t20_matches_details
    except Exception as e:
        print(e)
        print('Error in file: ' + filename)
        print('----------------------------------------\n')


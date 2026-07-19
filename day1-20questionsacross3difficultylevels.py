# # # Level 1 — Foundation (Basic Operations) — 7 Questions

# # # MARS pipeline has 45,000,000 rows total. 32,000,000 are loaded. How many remain?
# # ''''Ans:' marspipeline_total_rows = 45000000 
# # processed_rows = 32000000 
# # pending_loaded_rows = marspipeline_total_rows - processed_rows
# # # print(pending_loaded_rows)'''
# # # # A batch job processes 25,000 rows per run. If it runs 8 times, how many total rows processed?
# # # '''batch_job_per_run = 25000 
# # # runs_time = 8  #per day target
# # # total_rows_processed = batch_job_per_run * runs_time
# # # print(total_rows_processed)'''
# # # # Kelloggs pipeline runs for 2.25 hours daily. Over 6 days, what's the total runtime?
# # # '''kel_pie_daily_runhrs = 2.25
# # # total_days = 6 
# # # total_runtime = kel_pie_daily_runhrs * total_days
# # # print(total_runtime)'''
# # # # You have row_count = 12000000 and avg_load_time = 4.5. State which is int and which is float, and why.
# # # row_count = 12000000 # this is total row count is a int because this store the holl number
# # # # and rows can't be a flot the row always will count the holl number andholl number will process
# # # avg_load_time = 4.5  # is flot because if these both int will be also devide then still the outpout will become a
# # # # flot because this is the python beheviour. so here 4.5 is a flot.

# # # Add these three daily loads: Day1 = 1,200,000 rows, Day2 = 980,000 rows, Day3 = 1,450,000 rows. What's the 3-day total?
# # '''
# # daily_day1_rows_loaded = 1200000
# # daily_day2_rows_loaded = 980000
# # daily_day3_rows_loaded= 1450000

# # total_rows_loaded = daily_day1_rows_loaded + daily_day2_rows_loaded + daily_day3_rows_loaded
# # print(total_rows_loaded) '''

# # # A server costs ₹1200 per hour to run. If a pipeline runs for 7 hours, what's the total cost?
# # '''server_cost_per_hour = 1200
# # pipeline_runs = 7 
# # total_server_cost = server_cost_per_hour * pipeline_runs
# # print(total_server_cost)
# # '''
# # # 65000000 / 13 — run this in Python and state the exact output type (not just the number).
# # '''total_rows = 65000000
# # pipeline_runtime_hrs = 13
# # each_hours_row_processed = total_rows / pipeline_runtime_hrs
# # print(each_hours_row_processed) # the output is : 5000000.0'''

# # # Level 2 — Applied (Percentages & Multi-step) — 7 Questions

# # # Unilever pipeline: 91,000,000 total rows, 88,500,000 processed. Find remaining rows AND % complete.
# # # unilever_pipeline_total_rows = 91000000
# # # # total_processedrows = 88500000 
# # # # remaining_rows = unilever_pipeline_total_rows - total_processedrows
# # # # print(remaining_rows) # this will retun the the remaning rows yet to load

# # # # complete_per = total_processedrows/ unilever_pipeline_total_rows * 100
# # # # print(complete_per)

# # # # Last quarter's pipeline cost ₹450000. This quarter it's ₹540000. What's the % increase?
# # # # last_quarter_pepeline_cost = 450000
# # # # current_quarter = 540000
# # # # increase_per = current_quarter - last_quarter_pepeline_cost
# # # # print(increase_per)
# # # # # first we will find out the how much number has been incresed, then we will convert this number to the %
# # # # #thats the outpout, and below is the output
# # # # increase_perce = increase_per/ last_quarter_pepeline_cost * 100
# # # # print(increase_perce)
# # # # # A data quality check runs on 20,000,000 rows. 19,400,000 pass validation. What % failed?

# # # # You need to hit 90% completion on a 70,000,000-row pipeline. How many rows must be processed to hit exactly 90%?
# # # # Nielsen pipeline processed 40M rows in the morning run and 35M in the evening run out of 83M total. What's the combined % complete?
# # # # A pipeline's storage cost dropped from ₹80,000/month to ₹68,000/month. What's the % decrease?

# # # # If percent_complete = 72.5, what is percent_remaining? Show the formula, not just the answer.

# # # # percent_complete = 72.5
# # # # percent_remaining =  '?'

# # # # newVarable = percent_remaining = 100 - percent_complete
# # # # print(newVarable)  # 275862.0689655173, (27.5) is the remaining %

# # # # Level 3 — Interview-Style (Reasoning & Edge Cases) — 6 Questions

# # # # Without running any code, predict the output type (int or float) of: 100 / 4, 100 / 3, 4 * 25. Explain your reasoning for each before checking.
# # # # 100 / 4, 100 / 3 - float because devide behavious always flot in the python pyhton alwuyas will return the folt when we will the devide with int and any kind of number. 
# # # # 4 * 25 - int 
# # # # A colleague writes completion_percent = (total_rows % processed_rows) * 100 to calculate completion percentage. Explain in your own words why this is wrong, and what it should be instead.

# # # First of all we need to understand the percent funcation how works, completion_percent = (processed_rows / total_rows ) *100 is the output, because this is the correct funcation 

# # # why this it the correct funcation and my colleaguewrite the wrong, let me explain: bevcaue in percent calucation 

# # # % will give the reminder, not the percente on pyhton. where i alwsays configue erlier . / will device the data and return without reminder
# # # when we will to check the % of of 100 and slipt shares then % is the best because at the time we need reminder with each of. 

# # # i now this explaintion might be wrong but i understand the consept

# # # # True or False: "If a division result looks like a whole number (e.g., 100/4 = 25.0), Python will return it as an int." Justify your answer.
# # # Not yet extracly if division will look like a whole number still pyhton will return the flaot number 
# # # because thios is the pyhton beheviour bydefult
# # # # A pipeline dashboard shows "108% complete." Without knowing the exact numbers, explain what kind of mistake in the code likely caused this.
# # # yes so this % calculate worngly with varible = (total_rows / remaning_rows)*100
# # # where the correct method is (part / total)*100
# # # # You calculate percent_remaining = 12.5 and percent_complete = 86.5. These don't add up to 100. Walk through what could be wrong — name at least 2 possible bugs.
# # # first i will check the total rows and complete % of the rows, 
# # # 2nd I will check the - % formulr where is corrector not. because % should not go beyone of the 100%
# # # # Explain, as if to a new teammate who's never coded before, why int and float are treated differently in a data pipeline — use a real example of what could break if you mixed them up carelessly.

# # # # Yes, this is the very important for beggineres, because float bydefult is a diffrent behavirs, 
# # # if we didnot do proporly and ignore the claculation then the whole numbers will be goese worng and output as well. 
# # # on production this will impact on data and product as well. so crefully we should notice the int and float beheviours 



# # # Q10. 20,000,000 rows checked, 19,400,000 pass. What % failed?
# # # Total_row_checked =  20000000
# # # pass_rows = 19400000
# # # failedRowsNumber_count = Total_row_checked - pass_rows

# # # failed_rows_per = pass_rows / Total_row_checked
# # # print(failed_rows_per)

# # # Q11. Need 90% completion on 70,000,000 rows. How many rows must be processed?
# # # total_rows = 70000000
# # # target_percent = 90
# # # processed_rows = (target_percent / 100) * total_rows
# # # print(processed_rows)

# # # Q12. Nielsen: 40M morning + 35M evening out of 83M total. Combined % complete?

# # # Morning = 40
# # # Evening = 35 
# # # print(Morning+Evening) #Total 75M rows

# # Total_rows = 83000000
# # Row_processed = 75000000
# # combine_complete_per = Row_processed/ Total_rows * 100
# # print(combine_complete_per) #90.36144578313254
# # # Q13. Storage cost dropped from ₹80,000 to ₹68,000/month. % decrease?

# # erlier_storage_cost = 80000 
# # new_storage_cost = 68000
# # decrease_cost_number = erlier_storage_cost % new_storage_cost * 100
# # print(decrease_cost_number)


# # # erlier_storage_cost = 80000 
# # # new_storage_cost = 68000
# # # decrease_cost_number = erlier_storage_cost - new_storage_cost
# # # #print(decrease_cost) # 12000 total cost, now we will find the %
# # # decrese_cost = decrease_cost_number/ new_storage_cost * 100
# # # print(decrese_cost) #17.647058823529413



# # Q10. 20,000,000 rows checked, 19,400,000 pass. What % failed?

# total_row_checked  = 20000000
# row_passed = 19400000
# #first we will find the number of failled

# fail_rows_number = total_row_checked - row_passed

# # we get the fail number 

# failed_per = fail_rows_number/ total_row_checked * 100
# print(failed_per)

# # Q13. Storage cost dropped from ₹80,000 to ₹68,000/month. What's the % decrease?

# cost_old = 80000
# cost_new = 68000

# find_the_number_of_decrease = cost_old - cost_new
# print(find_the_number_of_decrease) #12000

# per_decrese = find_the_number_of_decrease / cost_old * 100
# print(per_decrese) #15.0
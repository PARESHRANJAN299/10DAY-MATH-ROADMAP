# Q1: A Kelloggs pipeline loaded 91M out of 96M rows. What is the completion %?

variable = 91 / 96 * 100

print(variable)
# 94.79166666666666 is the completion % 


# Q2: A Unilever data quality check found 45,000 duplicate rows out of 3,000,000 total rows.
#  What is the duplicate %?

# var = 1000000 / 3000000 * 100
# print(var) #1.5  i got the retrun ? but this is not correct right.


# # Q3: Last month, a batch job used 40 GB of storage. This month it used 52 GB. 
# # 
# # What is the percentage growth?
# old = 40
# new = 50
# growth = (new - old ) / old * 100
# print(growth)  #25.0

# growth = new - old
# # print(growth) - so part is 10 now . and part will devide with old

# v = 10 / 40 * 100
# print(v)




# # 🟢 Basic (straightforward part ÷ total)
# # Q1: A pipeline loaded 45 out of 50 files successfully. What is the completion %?

# total_files = 50
# loaded =  45
# total = loaded/ total_files * 100
# print(total) #90.0 is completetion
# # Q2: Out of 200 total columns in a table, 20 are marked as PII. What percentage of columns are PII?

# var = 20 / 200 * 100
# # print(var) answer = 10.0

# # Q3: A batch has 1000 rows, and 250 are null in one column. What is the null %?

# batch = 250 / 1000 * 100
# print(batch)

# 🟡 Medium (larger numbers, or requires spotting the right part/total)
# Q4: MARS pipeline processed 68,500,000 rows out of a total 72,000,000 rows expected. What is the completion %?

var = 68500000 / 72000000 * 100
# print(var) 95.13888888888889 (answer)
# Q5: A Databricks job has 15 tasks. 3 tasks failed.
#  What is the failure % and what is the success %? (both from the same numbers)
databricks_task = 15
failed = 3

failure = failed/ databricks_task * 100
# print(failure) failed = 20.0
success = (databricks_task- failed) / databricks_task * 100
# print(success) 80.0 is the success rate 

# Q6: A Unilever table has 12,000,000 rows. After deduplication, 11,760,000 remain. What percentage of rows were removed as duplicates?

unilever_table = 12000000
deduplication = 11760000
percentage = (unilever_table - deduplication)/ unilever_table * 100
# print(percentage) 2.0 rows were we removed as duplicate.


# 🔴 Hard (multi-step, or requires you to figure out what the "total" even is)
# Q7: Out of 5 CPG clients' pipelines (Unilever, MARS, Kelloggs, Nestle, PepsiCo), 
# only 4 completed successfully today. What % of clients had a successful run?
total_cpg = 5
completed = 4
successful_run = completed / total_cpg * 100
# print(successful_run) 80.0 is completed
# Q8: A Nielsen file was supposed to have 96,000,000 rows. Due to a partial load failure, only 3,840,000 rows are missing. What is the completion %? (hint: you're given the missing count, not the loaded count — figure out loaded first)
# Q9: A quality check ran on 3 tables: Table A (10,000 rows, 200 bad), Table B (50,000 rows, 500 bad), Table C (25,000 rows, 1,250 bad). What is the overall bad-row % across all three tables combined? (hint: combine totals first, don't average the 3 percentages directly)
# Q10: A subscription table had 8,000,000 active rows last quarter. This quarter, after churn, only 7,200,000 remain active — but 400,000 of those are new rows added this quarter. What percentage of last quarter's original rows are still active this quarter? (hint: figure out how many of the 7.2M are actually "old" rows first)
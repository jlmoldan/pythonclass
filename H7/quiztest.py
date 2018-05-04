




















# #
# # list_quiz.py:
# #
# #   Starting code H7-5
# #
#
# # Give short one-question quiz on HTT10 (Lists) to user
#
# quizquestion = input ("Are you ready for a quiz?  (y/n)")
# quizquestion = quizquestion.lower()
# if quizquestion == 'y':
#     #print ("yes")
#     print ()
#     print ("Givin the following information - what is printed by the following statement ")
#     print ()
#     print ("a_list = ['a', 'b', 'c', 'd', 'e', 'f']")
#     print ("print(a_list[3:])")
#     print ()
# # Maybe enter a while statement here - while correct = F loop.
# # Set another var - try again.  If F print please Try again......
# # if they select the correct one - set correct = T
#     correct = False
#     while correct =  False:
#         print()
#         print("a: ['b', 'c']")
#         print("b: ['a', 'b', 'c', 'd']")
#         print("c: ['d', 'e', 'f']")
#         print("d: ['a', 'b', 'c', 'd', 'e', 'f']")
#         print()
#         answer = input("which of the following is correct?")
#         answer = answer.lower()
#         if answer == "c":
#             print ("yea - good job")
#             correct = True
#             break
#         elif answer == "a":
#             print ("a: is incorrect because  the slice [1:3] would return ['b', 'c'].  Remember that the first index is the starting point for the")
#             print ("slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you")
#             print ("omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice")
#             print ("goes to the end of the sequence.")
#         elif answer == "b":
#             print ("b: is incorrect because the slice [:4] would return ['a', 'b', 'c', 'd'].  Remember that the first index is the starting point for the")
#             print ("slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you")
#             print ("omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice")
#             print ("goes to the end of the sequence.")
#         elif answer == "d":
#             print("d: is incorrect because [:] would return ['a', 'b', 'c', 'd', 'e', 'f']. Remember that the first index is the starting point for the")
#             print ("slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you")
#             print ("omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice")
#             print ("goes to the end of the sequence.")
#         else:
#             print ("incorrect value entered")
#
#     elif quizquestion == 'n':
#         print ("OK then, have a great day")
#     else:
#         print ("##########################")
#         print ("invalid selection")
#         print ("valid options are y or n")
#         print ("##########################")
#

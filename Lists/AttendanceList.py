#  A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom.
#  Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer
#  and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, 
#  saying that her list is in reverse order.The contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

Jamies_list.reverse()
Drews_list.extend(Jamies_list)
print(Drews_list)

# Arithmatic calculator by list
while True:
    first_input=int(input("Enter your First :- \n"))
    second_input=int(input("Enter your second :- \n"))

    operation_perform_1=(first_input)+(second_input)
    operation_perform_2=(first_input)- (second_input)
    operation_perform_3=(first_input)* (second_input)
    operation_perform_4=(first_input)/(second_input)
    operation_perform_5=(first_input)%(second_input)
    
    result_list={operation_perform_1, operation_perform_2,operation_perform_3,operation_perform_4,operation_perform_5}
    print(result_list)
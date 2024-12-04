def student_info(*args,**kwargs):
    if kwargs.get("operation")=='avg':
        return sum(args)/len(args)
    if kwargs.get("operation")=='total':
        return sum(args)
        # result = 0
        # for i in args:
        #     result += i
        # return result
print(student_info(45,43,44,operation='avg'))
print(student_info(45,43,44,operation='total'))
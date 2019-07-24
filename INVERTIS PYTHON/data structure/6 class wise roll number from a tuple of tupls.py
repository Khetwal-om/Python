from collections import defaultdict

classes =(
('v',1),
('vi',1),
('v',2)
)



class_roll=defaultdict(list)
for class_name,roll_id in classes:
    class_roll[class_name].append(class_roll)


print(class_roll)

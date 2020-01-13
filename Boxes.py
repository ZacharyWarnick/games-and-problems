'''
File: Boxes.py

Description: Outputs the greatest size groups of all subsets of boxes that fit within one another
'''

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def subs(superset):
    if superset == []:
        return [[]]

    x = subs(superset[1:])

    return x + [[superset[0]] + y for y in x]

def incrementingSize(box):

  for n in range(len(box)-1):
    if does_fit(box[n],box[n+1]):
      continue
    else:
      return False
  return True

def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()
  for box in box_list:
    box.sort()

  # create a list that will hold the nested boxes

  nested_boxes = []

  # create a variable for the size of the nested boxes
  size = 0

  # get all subsets of boxes

  subset_list = (subs(box_list))

  # for each subset check if they all fit and if it is the largest subset: increase the required size to be included
  print()
  for sub in subset_list:
    if incrementingSize(sub):
      nested_boxes.append(sub)
      if len(sub) > size:
        size = len(sub)

  #output ascending order or smallest box for easier comparison
  nested_boxes.sort()
  if size < 2:
    print("No nesting boxes.")
  else:
    print("Largest Subset of Nesting Boxes")
    for nested in nested_boxes:
      if len(nested) == size:
        print()
        for box in nested:
          print(box)

if __name__ == '__main__':
  main()
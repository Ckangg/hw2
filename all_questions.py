# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.278

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.03

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.24

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.03

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.07

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.722

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.17

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.722

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.321

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.17

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    #import utils as u
    tree = u.BinaryTree("smoking")
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    # Four leaves
    A.insert_left("yes")
    A.insert_right("no")
    B.insert_left("yes")
    B.insert_right("no")

    answer["tree"] = tree
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.425
    # Infogain
    answer["(b) x <= 0.2"] = 0.195
    answer["(b) x <= 0.7"] = 0.356
    answer["(b) y <= 0.6"] = 0.348

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "x=0.7"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    #import utils as u    
    tree = u.BinaryTree("x<=0.7")

    # Insert the left side of the tree
    y_06_left = tree.insert_left("y<=0.6")
    B = y_06_left.insert_left("B")  # Terminal node B
    x_02 = y_06_left.insert_right("x<=0.2")
    a_left = x_02.insert_right("A")  # Terminal node A
    y_08 = x_02.insert_left("y<=0.8")
    c_left = y_08.insert_left("C")  # Terminal node C
    b_right = y_08.insert_right("B")  # Terminal node B

    # Insert the right side of the tree
    y_03_right = tree.insert_right("y<=0.3")
    a_right = y_03_right.insert_left("A")  # Terminal node A
    y_06_right = y_03_right.insert_right("y<=0.6")
    c_right = y_06_right.insert_left("C")  # Terminal node C
    a_far_right = y_06_right.insert_right("A")  # Terminal node A
    #tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.491

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "if an attribute can give information, choose the lowest gini index of them. if an attribute cannot give information, ignore it even it is the lowest"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','nominal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = "0 means no angle, so it has absolutely zero point"

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continunous','quantitative','ratio']
    answer["f: explain"] = "there is a true zero point, the sea "

    answer["g"] = ['continuous','quantitative','ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete','quantitative','nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continunous','quantitative','ratio']
    answer["k: explain"] = ""

    answer["l"] = ['continunous','quantitative','ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete','qualitative','norminal']
    answer["m: explain"] = "it will not appear decimal number, it just a symbol for identification"

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "the accuracy in test dataset will show the ability of dealing with the unseen data, and the 0.82 in train data means that this model didn't study all the noises of the data, it didn't overfitting."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "the 0.85 and 0.81 are the averages of two dataset, so it cannot show the ability of dealing with unseen data, only the test data can show this ability. So when judged a model we should look at the accuracy in test data. "

    explain["c similarity"] = "in order to avoid overfitting"
    explain["c similarity explain"] = "they tend to select simple model, so that it will decrease the risk of being overfitting and increase the generalization"

    explain["c difference"] = "the way to realize and computation method"
    explain["c difference explain"] = "the MDL is based on the principles of information theory to choose the model, the pessimistic error estimate is adding a penalty term to avoid model be complexed, it can find a balance between complexity and ability "

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x<=0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y<=0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "B"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.06

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    #import utils as u
    tree = u.BinaryTree("x<=0.5")
    tree.insert_right("A")
    b = tree.insert_left("y<=0.4")
    b.insert_left("A")
    b.insert_right("B")
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.53

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Handedness"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

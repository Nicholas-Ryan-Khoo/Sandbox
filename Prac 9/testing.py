def change_case(string):
    return ''.join(['_' + i.upper() if i.isupper()
                    else i for i in string]).lstrip('_')


# Driver code
string = "GeeksForGeeks"
print(change_case(string))

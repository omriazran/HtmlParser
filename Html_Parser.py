"""
* omri azran
* 316098979
* 01
* ass7
"""

"""
* Function Name:print_user_file
* Input:links_dict
* Output:-
* Function Operation:print sort list for links in chosen file by the user
"""
def print_user_file(links_dict):
    user_file = input('enter file name:\n')
    links_dict[user_file].sort()
    print(links_dict[user_file])


"""
* Function Name:create_csv_file
* Input:links_dict
* Output:csv file
* Function Operation:create csv file from the links dictionary
"""
def create_csv_file(links_dict):
    str_csv = ""
    nums_of_items = 1
    for key , values in links_dict.items():
        if len(values) == 0:
            str_csv = str_csv + key
        else:
         str_csv = str_csv + key + ","
        for link in values:
            if link != values[len(values)-1]:
             str_csv = str_csv + link + ","
            else:
             str_csv = str_csv + link
        if nums_of_items != len(links_dict) :
             str_csv = str_csv + "\n"
        nums_of_items += 1
    csv_file = open("results.csv", "w")
    csv_file.write(str_csv)
    csv_file.close()



"""
* Function Name:init_exe
* Input:links_dict
* Output:-
* Function Operation:fill the dictionary when the keys are the file and the values 
are the links in the file
"""
def init_exe(links_dict):
    file_name = input('enter source file:\n')
    file = file2string(file_name)
    list = []
    # create  dictionary for file : links in file
    create_list_links(file, 0, list)
    links_dict[file_name] = list
    manage_dictionary(file_name, links_dict)



"""
* Function Name:file2string
* Input:file_name
* Output:string
* Function Operation:copy the file text to a string
"""
def file2string(file_name):
    original_file = open(file_name, 'r')
    file = original_file.read()
    original_file.close()
    return file


"""
* Function Name:create_list_links
* Input:string file , starting point for the find func,empty list
* Output:-
* Function Operation:fill the list in which links exist in the current file
"""
def create_list_links(file , start,list):

    if file.find('href=', start) == -1:
        return
    start = file.find('href=',start)
    start = file.find('"', start)
    end = file.find('"', start+1)
    link = file[start+1:end]
    list.append(link)
    create_list_links(file , start,list)


"""
* Function Name:manage_dictionary
* Input:file name and dictionary
* Output:-
* Function Operation:fill the dictionary the key are the name of the file and the values are the links
to other files
"""
def manage_dictionary(file_name, links_dict):
  for val in links_dict[file_name]:
      if val is None:
       return
      if val in links_dict:
       return
      string_file = file2string(val)
      emptylist = []
      create_list_links(string_file,0,emptylist)
      links_dict[val] = emptylist
      manage_dictionary(val, links_dict)
  return


# "main"
# create empty dictionary of links
links_dict = {}
init_exe(links_dict)
create_csv_file(links_dict)
print_user_file(links_dict)











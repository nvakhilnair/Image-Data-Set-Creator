import os  
def rename_file(path,fname,search_query):
    files = os.listdir(path)
    count = 1
    for file in files:
        try:
            filename = fname + '_' + str(count) + ".jpg"
        except:
            filename = search_query + '_' + str(count) + ".jpg"
        src = path + file
        dst = path + filename 
        os.rename(src, dst) 
        count = count + 1
  
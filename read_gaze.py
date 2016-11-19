##following method will read the gaze data files 
def readGazeData(fName):
    samples = []
    with open(fName,'r') as f :
        try :
            for line in f :
                contents = line.split(',')
                x = contents[0]
                y = contents[1]
                ##only read the first 2 columns of data ,ignore time stamp for now 
                samples.append([x,y])
        except ValueError :
            pass
    return samples


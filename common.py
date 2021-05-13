import os


def writeFile(responseMessage, filepath, fileData):
    try:
        with open(file=filepath, mode='xb') as uploadF:
            for line in fileData:
                uploadF.write(line)

        responseMessage += ": SUCCESS - file has been sent successfully. \n"
    except FileExistsError as e:
        responseMessage += ": FAILURE - file already exists. \n " + str(e)
    except Exception as e:
        responseMessage += ": FAILURE - something has gone wrong. \n" + str(e)
    finally:
        print(responseMessage)


def readFile(responseMessage, requestFilePath):
    try:
        requestFile = open(file=requestFilePath, mode='rb')
        requestFileData = requestFile.readlines()
        return requestFileData

        responseMessage += ": SUCCESS - file data read successfully. \n"
    except FileNotFoundError as e:
        responseMessage += ": FAILURE - file doesn't exist. \n " + str(e)
    except Exception as e:
        responseMessage += ": FAILURE - something has gone wrong. \n " + str(e)
    finally:
        print(responseMessage)


def listDirectoryContents(responseMessage):
    print(responseMessage + ": Listing 1st-level directory contents. \n")

    for entity in os.listdir():
        print(entity)

    print(responseMessage + ": Finished listing directory contents. \n")

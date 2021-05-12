def writeFile(addr, filepath, fileData):
    responseMessage = str(addr)

    try:
        with open(file=filepath, mode='xb') as uploadF:
            for line in fileData:
                uploadF.write(line)

        responseMessage += ": SUCCESS - file has been sent successfully"
    except FileExistsError:
        responseMessage += ": FAILURE - file already exists"
    except:
        responseMessage += ": FAILURE - something has gone wrong"
    finally:
        print(responseMessage)


def readFile(addr, requestFilePath):
    responseMessage = addr

    try:
        requestFile = open(file=requestFilePath, mode='rb')
        requestFileData = requestFile.readlines()
        return requestFileData

        responseMessage += ": SUCCESS - file data read successfully"
    except FileNotFoundError:
        responseMessage += ": FAILURE - file doesn't exist"
    except:
        responseMessage += ": FAILURE - something has gone wrong"
    finally:
        print(responseMessage)

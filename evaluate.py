import sys
import mlp
import numpy as np

def testMLP(dataFileName,nhidden):
    dataText = np.loadtxt(dataFileName,delimiter=',')
    target = np.zeros((np.shape(dataText)[0],2))
    indices = np.where(dataText[:,-1]==0)
    target[indices,0] = 1
    indices = np.where(dataText[:,-1]==1)
    target[indices,1] = 1

    #print dataText
    # 5 fold validation
    val_error = []
    TP = []
    TN = []
    FP = []
    FN = []
    order = range(np.shape(dataText)[0])
    np.random.shuffle(order)
    dataText = dataText[order,:]
    dataText = dataText[:,:-1]
    target = target[order,:]
    for i in range(5):
        valid = dataText[i*len(dataText)/5:(i+1)*len(dataText)/5]
        validt = target[i*len(target)/5:(i+1)*len(target)/5]
        train = np.vstack((dataText[:i*len(dataText)/5],dataText[(i+1)*len(dataText)/5:]))
        traint = np.vstack((target[:i*len(target)/5],target[(i+1)*len(target)/5:]))
        net = mlp.mlp(train,traint,nhidden,outtype='softmax')
        val_error.append(net.earlystopping(train,traint,valid,validt,0.3))
        cm = net.confmat(valid,validt)
        TP.append(cm[0][0])
        FN.append(cm[0][1])
        FP.append(cm[1][0])
        TN.append(cm[1][1])
    return np.mean(val_error),np.sum(TP),np.sum(FP),np.sum(TN),np.sum(FN)

def main():
    dataFileName = sys.argv[1]
    nhidden = int(sys.argv[2])
    
    val_error = []
    TP = []
    TN = []
    FP = []
    FN = []
    sensitivity = []
    specificity = []
    accuracy = []
    for i in range(20):
        result = testMLP(dataFileName,nhidden)
        val_error.append(result[0])
        TP.append(result[1])
        FN.append(result[2])
        FP.append(result[3])
        TN.append(result[4])

    tp = np.mean(TP)
    tn = np.mean(TN)
    fp = np.mean(FP)
    fn = np.mean(FN)
    print "===========result========"
    print "Mean error:", np.mean(val_error)
    print "Standard Deviation:", np.std(val_error)
    print "Max error:", max(val_error)
    print "Min error:", min(val_error)
    print "===========performance========"
    print "TP:", tp," TN:",tn,"FP:", fp," FN:",fn
    print "sensitivity:", tp/(tp+fn)
    print "specificity:", tn/(tn+fp)
    print "accuracy:", (tp+tn)/(tp+tn+fp+fn)
main()

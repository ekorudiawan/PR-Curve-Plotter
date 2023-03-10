from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc
import matplotlib as mpl
import matplotlib.pyplot as plt

magenta_recall_11 = [0.0000, 0.1000, 0.2000, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000, 0.8000, 0.9000, 1.0000]
magenta_precision_11 = [1.0000, 0.9955, 0.9955, 0.9901, 0.9860, 0.9781, 0.7441, 0.0000, 0.0000, 0.0000, 0.0000]
cyan_recall_11 = [0.0000, 0.1000, 0.2000, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000, 0.8000, 0.9000, 1.0000]
cyan_precision_11 = [1.0000, 1.0000, 1.0000, 1.0000, 0.9949, 0.9881, 0.9576, 0.8580, 0.0000, 0.0000, 0.0000]

magenta_recall_101 = [
0.0000, 0.0100, 0.0200, 0.0300, 0.0400, 0.0500, 0.0600, 0.0700, 0.0800, 0.0900,
0.1000, 0.1100, 0.1200, 0.1300, 0.1400, 0.1500, 0.1600, 0.1700, 0.1800, 0.1900,
0.2000, 0.2100, 0.2200, 0.2300, 0.2400, 0.2500, 0.2600, 0.2700, 0.2800, 0.2900,
0.3000, 0.3100, 0.3200, 0.3300, 0.3400, 0.3500, 0.3600, 0.3700, 0.3800, 0.3900,
0.4000, 0.4100, 0.4200, 0.4300, 0.4400, 0.4500, 0.4600, 0.4700, 0.4800, 0.4900,
0.5000, 0.5100, 0.5200, 0.5300, 0.5400, 0.5500, 0.5600, 0.5700, 0.5800, 0.5900,
0.6000, 0.6100, 0.6200, 0.6300, 0.6400, 0.6500, 0.6600, 0.6700, 0.6800, 0.6900,
0.7000, 0.7100, 0.7200, 0.7300, 0.7400, 0.7500, 0.7600, 0.7700, 0.7800, 0.7900,
0.8000, 0.8100, 0.8200, 0.8300, 0.8400, 0.8500, 0.8600, 0.8700, 0.8800, 0.8900,
0.9000, 0.9100, 0.9200, 0.9300, 0.9400, 0.9500, 0.9600, 0.9700, 0.9800, 0.9900,
1.0000]

magenta_precision_101 = [
1.0000, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 
0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955, 0.9955,
0.9955, 0.9955, 0.9916, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901,
0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9901, 0.9881,
0.9860, 0.9851, 0.9851, 0.9851, 0.9851, 0.9840, 0.9840, 0.9824, 0.9807, 0.9794,
0.9781, 0.9781, 0.9750, 0.9672, 0.9610, 0.9368, 0.9245, 0.8981, 0.8529, 0.8042,
0.7456, 0.7013, 0.6684, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0.0000]

cyan_recall_101 = [
0.0000, 0.0100, 0.0200, 0.0300, 0.0400, 0.0500, 0.0600, 0.0700, 0.0800, 0.0900,
0.1000, 0.1100, 0.1200, 0.1300, 0.1400, 0.1500, 0.1600, 0.1700, 0.1800, 0.1900,
0.2000, 0.2100, 0.2200, 0.2300, 0.2400, 0.2500, 0.2600, 0.2700, 0.2800, 0.2900,
0.3000, 0.3100, 0.3200, 0.3300, 0.3400, 0.3500, 0.3600, 0.3700, 0.3800, 0.3900,
0.4000, 0.4100, 0.4200, 0.4300, 0.4400, 0.4500, 0.4600, 0.4700, 0.4800, 0.4900,
0.5000, 0.5100, 0.5200, 0.5300, 0.5400, 0.5500, 0.5600, 0.5700, 0.5800, 0.5900,
0.6000, 0.6100, 0.6200, 0.6300, 0.6400, 0.6500, 0.6600, 0.6700, 0.6800, 0.6900,
0.7000, 0.7100, 0.7200, 0.7300, 0.7400, 0.7500, 0.7600, 0.7700, 0.7800, 0.7900,
0.8000, 0.8100, 0.8200, 0.8300, 0.8400, 0.8500, 0.8600, 0.8700, 0.8800, 0.8900,
0.9000, 0.9100, 0.9200, 0.9300, 0.9400, 0.9500, 0.9600, 0.9700, 0.9800, 0.9900,
1.0000]

cyan_precision_101 = [
1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000,
1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000,
1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000,
1.0000, 1.0000, 1.0000, 1.0000, 0.9974, 0.9974, 0.9974, 0.9974, 0.9974, 0.9949,
0.9949, 0.9928, 0.9928, 0.9909, 0.9909, 0.9888, 0.9881, 0.9881, 0.9881, 0.9881,
0.9881, 0.9881, 0.9852, 0.9852, 0.9852, 0.9802, 0.9786, 0.9720, 0.9664, 0.9650,
0.9606, 0.9505, 0.9443, 0.9378, 0.9301, 0.9219, 0.9149, 0.9008, 0.8864, 0.8710,
0.8580, 0.8515, 0.8387, 0.8165, 0.7960, 0.7722, 0.7403, 0.0000, 0.0000, 0.0000,
0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
0]

def main():
    auc_magenta_101 = auc(magenta_recall_101, magenta_precision_101)
    auc_cyan_101 = auc(cyan_recall_101, cyan_precision_101)
    print("AUC Magenta 101-Points Interpolation", auc_magenta_101)
    print("AUC Cyan 101-Points Interpolation", auc_cyan_101)

    mpl.rcParams['font.family'] = 'Avenir'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2

    plt.plot(magenta_recall_101, magenta_precision_101, marker='.', label='Magenta Robot')
    plt.plot(cyan_recall_101, cyan_precision_101, marker='.', label='Cyan Robot')
    plt.title("101-Points Interpolation PR Curve")
    # axis labels
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    # show the legend
    plt.legend()
    # show the plot
    # plt.show()

    plt.savefig('101-Points Interpolation PR-Curve.png', dpi=300, transparent=False, bbox_inches='tight')


    # #create dataset with 5 predictor variables
    # X, y = datasets.make_classification(n_samples=1000,
    #                                     n_features=4,
    #                                     n_informative=3,
    #                                     n_redundant=1,
    #                                     random_state=0)

    # #split dataset into training and testing set
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3,random_state=0)

    # #fit logistic regression model to dataset
    # classifier = LogisticRegression()
    # classifier.fit(X_train, y_train)

    # #use logistic regression model to make predictions
    # y_score = classifier.predict_proba(X_test)[:, 1]
    # #calculate precision and recall
    # precision, recall, thresholds = precision_recall_curve(y_test, y_score)
    # print("Recall : ", recall)
    # print("Precision : ", precision)
    # #create precision recall curve
    # fig, ax = plt.subplots()
    # ax.plot(recall, precision, color='purple')

    # #add axis labels to plot
    # ax.set_title('Precision-Recall Curve')
    # ax.set_ylabel('Precision')
    # ax.set_xlabel('Recall')

    # #display plot
    # plt.show()

if __name__ == "__main__":
    main()
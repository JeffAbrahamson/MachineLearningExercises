from basePredictor import BasePredictor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class RandomForestPredictor(BasePredictor):

    def _generate_classifier(self):
        forest = RandomForestClassifier(n_estimators=100, random_state=42)
        return forest.fit(self.x_train, self.y_train)

    def _predict(self, classifiers):
        stats = {'TP' :0, 'FP' : 0, 'TN': 0, 'FN': 0}
        for elem in self.test_values:
            predicted = classifiers.predict([elem[0]])
            if predicted[0] == elem[1]:
                stats['TP'] +=1
            else:
                stats['FP'] +=1
        correctness = (stats['TP']/len(self.test_values)*100)
        precision = (stats['TP']/(stats['TP'] + stats['FP'])) *100
        recall = (stats['TP']/(stats['TP'] +stats['FN']))*100
        f_measure = ((precision * recall)/(precision + recall))*2
        return {'correctness' :  correctness, 'precision' : precision,
                'recall' : recall, 'f1' : f_measure}






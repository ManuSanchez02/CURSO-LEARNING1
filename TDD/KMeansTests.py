import unittest
import numpy as np


def next_centroid(cluster):
    return tuple(np.mean(cluster, axis=0))


def distance(centroid, sample):
    return np.linalg.norm(np.subtract(centroid, sample))


def next_centroid(cluster):
    return tuple(np.mean(cluster, axis=0))


def distance(centroid, sample):
    return np.linalg.norm(np.subtract(centroid, sample))


class KMeansModel:

    def __init__(self):
        self.clusters = None
        self.centroids = None
        self.trained = False

    def _update_clusters(self, samples, max_iter):
        reassignment = True
        j = 0
        while reassignment is True and j < max_iter:
            reassignment = False

            old_clusters = self.clusters
            new_clusters = [[] for _ in range(len(self.clusters))]

            for sample in samples:
                closest_centroid = self._closest_centroid(sample)
                new_clusters[closest_centroid].append(sample)

                if not np.isin(sample, old_clusters[closest_centroid]).any():
                    reassignment = True

            self.clusters = new_clusters

            for i in range(len(self.centroids)):
                self.centroids[i] = next_centroid(self.clusters[i])

            j += 1

    def _closest_centroid(self, sample):
        min_dist = distance(self.centroids[0], sample)
        closest_centroid = 0
        for i in range(1, len(self.centroids)):
            current_dist = distance(self.centroids[i], sample)
            if min_dist > current_dist:
                min_dist = current_dist
                closest_centroid = i
        return closest_centroid

    def train(self, samples, n_clusters, max_iter, initial_centroids=None):
        if len(samples) == 0:
            raise ValueError("La lista de muestras no debe estar vacía")

        if initial_centroids is not None:
            self.centroids = initial_centroids
        else:

            self.centroids = samples[np.random.choice(np.arange(len(samples)), n_clusters, replace=False)]

        if self.clusters is None:
            self.clusters = [[] for _ in range(n_clusters)]

        self._update_clusters(samples, max_iter)

        self.trained = True

        return [tuple(centroid) for centroid in self.centroids]

    def process(self, sample):
        if len(sample) == 0:
            raise ValueError("El argumento no debe estar vacío")

        if not self.trained:
            raise ValueError("Primero hay que entrenar el modelo")

        return self._closest_centroid(sample)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.model = KMeansModel()

    def test_KMeansTrainRaisesException_WhenGivenNoInput(self):
        self.assertRaises(ValueError, self.model.train, [], 2, 10)

    def test_KMeansFor2ClustersAnd1Feature_TrainReturnsCentroids_WhenGivenMinimumInput(self):
        samples = [[0], [5]]
        centroids = self.model.train(samples, 2, 10, initial_centroids=[[0], [5]])

        self.assertEqual({(0,), (5,)}, set(centroids))

    def test_KMeansFor2ClustersAnd1Feature_TrainReturnsCentroids_WhenGivenMultipleInputs(self):
        samples = [[0], [1], [9], [10]]
        centroids = self.model.train(samples, 2, 20, initial_centroids=[[0], [10]])

        self.assertEqual({(0.5,), (9.5,)}, set(centroids))

    def test_KMeansFor2ClustersAnd1Feature_ProcessRaisesException_WhenGivenNoInput(self):
        self.assertRaises(ValueError, self.model.process, [])

    def test_KMeansFor2ClustersAnd1Feature_ProcessReturnsCluster_WhenTrainedAndGivenInput(self):
        samples = [[0], [1], [2], [18], [19], [20]]
        self.model.train(samples, 2, 20, initial_centroids=[[2], [18]])

        self.assertEqual(0, self.model.process([5]))

    def test_KMeansFor2ClustersAnd1Feature_ProcessRaisesException_WhenNotTrainedAndGivenInput(self):
        self.assertRaises(ValueError, self.model.process, [4])

    def test_KMeansFor2ClustersAnd2Features_TrainReturnsCentroids_WhenGivenMinimumInput(self):
        samples = [[0, 0], [10, 10]]
        centroids = self.model.train(samples, 2, 10, initial_centroids=[[0, 0], [10, 10]])

        self.assertEqual({(0, 0), (10, 10)}, set(centroids))

    def test_KMeansFor2ClustersAnd2Features_TrainReturnsCentroids_WhenGivenMultipleInputs(self):
        samples = [[0, 0], [0, 1], [1, 0], [1, 1], [10, 10], [10, 11], [11, 10], [11, 11]]
        centroids = self.model.train(samples, 2, 10, initial_centroids=[[0, 0], [10, 10]])

        self.assertEqual({(0.5, 0.5), (10.5, 10.5)}, set(centroids))

    def test_KMeansFor3ClustersAnd2Features_TrainReturnsCentroids_WhenGivenMinimumInput(self):
        samples = [[0, 0], [1, 1], [5, 5], [6, 6], [10, 10], [11, 11]]
        centroids = self.model.train(samples, 3, 10, initial_centroids=[[0, 0], [5, 5], [10, 10]])

        self.assertEqual({(0.5, 0.5), (5.5, 5.5), (10.5, 10.5)}, set(centroids))

    def test_KMeansFor3ClustersAnd2Features_TrainReturnsCentroids_WhenGivenMultipleInput(self):
        samples = [[0, 0], [0, 1], [1, 0], [1, 1], [10, 10], [10, 11], [11, 10], [11, 11], [20, 20], [20, 21], [21, 20], [21, 21]]
        centroids = self.model.train(samples, 3, 10, initial_centroids=[[0, 0], [11, 10], [20, 21]])

        self.assertEqual({(0.5, 0.5), (10.5, 10.5), (20.5, 20.5)}, set(centroids))

    def test_KMeansForMultipleClustersAndMultipleFeatures_TrainReturnsCentroids_WhenGivenMinimumInput(self):
        samples = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1],
                   [10, 10, 10], [10, 10, 11], [10, 11, 10], [10, 11, 11], [11, 10, 10], [11, 10, 11], [11, 11, 10], [11, 11, 11],
                   [20, 20, 20], [20, 20, 21], [20, 21, 20], [20, 21, 21], [21, 20, 20], [21, 20, 21], [21, 21, 20], [21, 21, 21]]
        centroids = self.model.train(samples, 3, 10, initial_centroids=[[0, 0, 0], [11, 11, 11], [21, 21, 21]])

        self.assertEqual({(0.5, 0.5, 0.5), (10.5, 10.5, 10.5), (20.5, 20.5, 20.5)}, set(centroids))


if __name__ == '__main__':
    unittest.main()

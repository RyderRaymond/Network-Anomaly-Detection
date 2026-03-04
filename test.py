import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load data
# df = pd.read_csv("NSL_KDD_Train.csv")
df = pd.read_csv("Network_anomaly_data.csv")
# Encode target variable
df['attack_type'] = df['attack'].apply(lambda x: 'normal' if x == 'normal' else 'attack')
# Encode categorical features
for col in ['protocoltype', 'service', 'flag']:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
# Drop irrelevant columns
features = df.drop(columns=['attack', 'lastflag', 'attack_type'])
target = df['attack_type']
# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

print(target)

import matplotlib.pyplot as plt
import seaborn as sns

# Class distribution
# sns.countplot(x='attack_type', data=df)
# plt.title('Class Distribution')
# plt.show()
# # Correlation heatmap
# plt.figure(figsize=(12, 10))
# sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
# plt.title('Feature Correlation Heatmap')
# plt.show()
# # Pairplot for selected features
# sampled_df = df.sample(500)
# sns.pairplot(sampled_df[['duration', 'src_bytes', 'dst_bytes', 'attack_type']], hue='attack_type')
# plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

print("X_train")
print(X_train)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
#print(classification_report(y_test, y_pred))
#print(confusion_matrix(y_test, y_pred))


# from sklearn.ensemble import IsolationForest

# isf = IsolationForest(contamination=0.1)
# isf.fit(X_train)
# anomaly_scores = isf.decision_function(X_test)
# unsup_pred = isf.predict(X_test)

# from sklearn.cluster import KMeans

# kmeans = KMeans(n_clusters=5, random_state=42)
# kmeans.fit(features_scaled)
# df['cluster'] = kmeans.predict(features_scaled)
# features_clustered = np.hstack((features_scaled, df['cluster'].values.reshape(-1, 1)))

# import streamlit as st

# st.title("Network Intrusion Detection")
# duration = st.number_input('Duration')
# protocol_type = st.selectbox('Protocol Type', ['tcp', 'udp', 'icmp'])
# service = st.text_input('Service')
# flag = st.selectbox('Flag', ['SF', 'S0', 'REJ'])
# src_bytes = st.number_input('Source Bytes')
# dst_bytes = st.number_input('Destination Bytes')
# input_data = [duration, 0, 0, 0, src_bytes, dst_bytes]
# if st.button('Predict'):
#     pred = model.predict([input_data])
#     st.write('Prediction:', pred[0])


# from sklearn.neighbors import LocalOutlierFactor
# lof = LocalOutlierFactor(n_neighbors=20)
# lof_pred = lof.fit_predict(features_scaled)

# from sklearn.cluster import DBSCAN
# db = DBSCAN(eps=0.5, min_samples=5).fit(features_scaled)
# from sklearn.mixture import GaussianMixture
# gmm = GaussianMixture(n_components=2)
# gmm.fit(features_scaled)
# gmm_pred = gmm.predict(features_scaled)

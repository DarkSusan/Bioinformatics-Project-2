import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def rf_mycorrhizae(input_file, num_estimators = 100, rand_state=42, size_of_test=0.3, mycorrhizae_weight = 1, non_mycorrhizae_weight = 1):
    print("------------------------------------------")
    print(f"\n{input_file.split(".")[0].lstrip("filtered").rstrip("mycorrhizae").replace("_", " ")}\n")
    print("------------------------------------------")
    data = pd.read_csv(input_file, sep=',', header=0)

    X = data.iloc[:, 1:]  # All columns except the first
    y = data.iloc[:, 0]  # First column

    # Test parameters
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size_of_test, random_state=rand_state)
    print(f"Total number of test samples: {len(y_test)}")

    # Training parameters
    clf = RandomForestClassifier(n_estimators=num_estimators, random_state=rand_state, n_jobs=16,
                                 class_weight={'mycorrhizae': mycorrhizae_weight, 'non_mycorrhizae': non_mycorrhizae_weight})
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    # Evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nGenerating Confusion Matrix\n")
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

    # Feature importance
    importances = clf.feature_importances_
    feat_names = X.columns
    feat_imp_df = pd.DataFrame({'Feature': feat_names, 'Importance': importances})
    feat_imp_df = feat_imp_df.sort_values(by='Importance', ascending=False)
    print(f"\nTop 10 Important Features:\n{feat_imp_df.head(10)}")

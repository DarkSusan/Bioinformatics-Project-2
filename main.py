import parser
import randomforest

if __name__ == '__main__':
    files_features = [("Secreted_CAZymes.csv", "AA1"), ("Secreted_Proteases.csv", "A01A"), ("Secreted_lipase.csv", "GGGX|ABH01"), ("SSPs.csv", "00023_12796_13606_13637_13857"), ]

    for file, features_header in files_features:
        filtered_rows, header = parser.ecology_filter(file, features_header)
        parser.mycorrhizae_filter(filtered_rows, header, f"filtered_{file.split('.')[0]}_mycorrhizae.csv")

        randomforest.rf_mycorrhizae(f"filtered_{file.split('.')[0]}_mycorrhizae.csv", num_estimators=1000, rand_state=42, size_of_test=0.3, mycorrhizae_weight=0.8, non_mycorrhizae_weight=1)


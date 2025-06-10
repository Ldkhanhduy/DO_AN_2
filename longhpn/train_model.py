import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score
import joblib
import re

# Đọc và xử lý dữ liệu
# file_path = "/home/long/Documents/DA2/preprocessed_laptop.xlsx"

def load_and_preprocess_data(file_path):
    # Đọc file Excel
    df = pd.read_excel(file_path, engine="openpyxl")
    
    # Làm sạch và chuẩn hóa dữ liệu
    def clean_screen_size(screen):
        if isinstance(screen, str):
            return float(re.findall(r'(\d+\.?\d*)', screen)[0])
        return screen
    df['Screen_Size'] = df['Screen'].apply(clean_screen_size)
    
    # Chuyển đổi cột phân loại thành số
    categorical_cols = ['Brand', 'CPU', 'Gpu', 'Os_sys']
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le
    
    # Tạo biến mục tiêu dựa trên nhu cầu sử dụng
    def assign_use_case(row):
        cpu_score = row['cpu_tier']
        gpu_score = row['gpu_tier']
        ram = row['RAM']
        rom = row['ROM']
        
        # Chơi game: CPU mạnh, GPU mạnh, RAM >=16GB, ROM >=512GB
        if cpu_score >= 1 and gpu_score >= 1 and ram >= 16 and rom >= 512:
            return 'Chơi game'
        # Thiết kế đồ họa: CPU mạnh, GPU khá, RAM >=16GB, màn hình độ phân giải cao
        elif cpu_score >= 1 and ram >= 16 and row['screen_tier'] >= 2:
            return 'Thiết kế đồ họa'
        # Văn phòng: CPU trung bình, GPU tích hợp, RAM >=8GB
        elif cpu_score >= 0 and gpu_score <= 0 and ram >= 8:
            return 'Văn phòng'
        # Sinh viên CNTT: CPU trung bình, bất kỳ GPU, RAM >=8GB, ROM >=256GB
        elif cpu_score >= 0 and ram >= 8 and rom >= 256:
            return 'Sinh viên CNTT'
        else:
            return 'Văn phòng'  # Mặc định
    
    df['Use_Case'] = df.apply(assign_use_case, axis=1)
    
    # Đặc trưng và mục tiêu
    features = ['CPU', 'Gpu', 'RAM', 'ROM', 'Screen_Size', 'cpu_tier', 'gpu_tier', 'screen_tier']
    X = df[features]
    y = df['Use_Case']
    
    return df, X, y, label_encoders

# Huấn luyện mô hình Random Forest
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Khởi tạo và huấn luyện mô hình
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # Đánh giá mô hình
    y_pred = rf.predict(X_test)
    precision = precision_score(y_test, y_pred, average='weighted')
    print(f"Độ chính xác (Precision Score): {precision:.4f}")
    
    return rf, X_train.columns

# Lưu mô hình và bộ mã hóa
def save_model_and_encoders(model, encoders, feature_columns):
    joblib.dump(model, 'rf_model.pkl')
    joblib.dump(encoders, 'label_encoders.pkl')
    joblib.dump(feature_columns, 'feature_columns.pkl')

def main():
    # file_path = "/home/long/Documents/DA2/preprocessed_laptop.xlsx"
    file_path = "D:\Subject\Year 3\Do_an_2\dataset\laptop_data_results.xlsx"
    df, X, y, label_encoders = load_and_preprocess_data(file_path)
    model, feature_columns = train_model(X, y)
    save_model_and_encoders(model, label_encoders, feature_columns)
    print("Mô hình và bộ mã hóa đã được lưu thành công.")

if __name__ == "__main__":
    main()
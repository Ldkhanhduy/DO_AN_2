import streamlit as st
import pandas as pd
import joblib
import re
import numpy as np
# Tải mô hình và bộ mã hóa
@st.cache_resource
def load_model_and_encoders():
    model = joblib.load('rf_model.pkl')
    encoders = joblib.load('label_encoders.pkl')
    feature_columns = joblib.load('feature_columns.pkl')
    return model, encoders, feature_columns

# Xử lý dữ liệu đầu vào
def preprocess_input(df, encoders, feature_columns):
    df = df.copy()
    df['Screen_Size'] = df['Screen'].apply(lambda x: float(re.findall(r'(\d+\.?\d*)', x)[0]) if isinstance(x, str) else x)
    
    for col in ['Brand', 'CPU', 'Gpu', 'Os_sys']:
        if col in encoders:
            df[col] = df[col].map(lambda x: encoders[col].transform([x])[0] if x in encoders[col].classes_ else -1)
    
    return df[feature_columns]

# Ứng dụng Streamlit chính
def main():
    st.title("Hệ thống Gợi ý Laptop")
    st.write("Chọn nhu cầu sử dụng để nhận gợi ý laptop phù hợp.")
    
    # Tải mô hình và bộ mã hóa
    model, encoders, feature_columns = load_model_and_encoders()
    
    # Tải dữ liệu
    df = pd.read_excel("D:\Subject\Year 3\Do_an_2\dataset\laptop_data_results.xlsx", engine="openpyxl")
    
    # Người dùng chọn nhu cầu
    use_case = st.selectbox("Chọn Nhu Cầu Sử Dụng", ['Chơi game', 'Văn phòng', 'Thiết kế đồ họa', 'Sinh viên CNTT'])
    
    if st.button("Nhận Gợi Ý"):
        # Xử lý dữ liệu
        X = preprocess_input(df, encoders, feature_columns)
        
        # Dự đoán nhu cầu
        predictions = model.predict(X)
        
        # Lọc các laptop phù hợp với nhu cầu được chọn
        recommended = df[(predictions == use_case)&((df['price_assessment']=="Phù hợp")|(df['price_assessment']=="Rẻ"))].head(5)
        
        if not recommended.empty:
            st.subheader(f"Top 5 Laptop Gợi Ý cho {use_case}")
            for _, row in recommended.iterrows():
                st.write(f"**Tên**: {row['Name']}")
                st.write(f"**Thương hiệu**: {row['Brand']}")
                st.write(f"**CPU**: {row['CPU']}")
                st.write(f"**GPU**: {row['Gpu']}")
                st.write(f"**RAM**: {row['RAM']} GB")
                st.write(f"**Bộ nhớ**: {row['ROM']} GB")
                st.write(f"**Màn hình**: {row['Screen']}")
                st.write(f"**Giá**: {row['Prices']:.2f} VND")
                st.write(f"**Đánh giá**: {row['price_assessment']}")
                st.write(f"**Link**: [Xem Sản Phẩm]({row['links-href']})")
                st.write("---")
        else:
            st.write("Không tìm thấy laptop phù hợp cho nhu cầu này.")

if __name__ == "__main__":
    main()
import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نظام إدارة الكتب", layout="wide")

# إضافة اسم المستخدم في الشريط الجانبي
st.sidebar.title("👤 المستخدم: ENG-ABDALLUH MUSHTAQ")

# إنشاء القائمة الجانبية
options = ["الصفحة الرئيسية", "إضافة كتاب جديد", "أرشيف الكتب"]
selected_option = st.sidebar.radio("اختر القسم:", options)

# محتوى الصفحة الرئيسية
st.title("📚 نظام إدارة الكتب")

if selected_option == "الصفحة الرئيسية":
    st.write("مرحبًا بك في نظام إدارة الكتب!")

elif selected_option == "إضافة كتاب جديد":
    st.subheader("📖 إضافة كتاب جديد")
    title = st.text_input("عنوان الكتاب:")
    author = st.text_input("اسم المؤلف:")
    
    # رفع ملف PDF
    pdf_file = st.file_uploader("📂 رفع ملف PDF للكتاب", type=["pdf"])

    # إدخال رابط فيديو يوتيوب
    youtube_link = st.text_input("🎬 رابط فيديو يوتيوب الخاص بالكتاب:")

    if st.button("حفظ الكتاب"):
        if pdf_file:
            st.success(f"تم حفظ الكتاب: {title} - {author} مع ملف PDF!")
        if youtube_link:
            st.success(f"تم حفظ رابط الفيديو: {youtube_link}")

elif selected_option == "أرشيف الكتب":
    st.subheader("📜 أرشيف الكتب")
    st.write("📂 هنا يمكنك عرض جميع الكتب المخزنة.")

# تشغيل التطبيق
if __name__ == "__main__":
    st.write("🔹 تطبيق خاص بـ ENG-ABDALLUH MUSHTAQ 🚀")
import streamlit as st

st.set_page_config(page_title="Web đặt đồ uống", page_icon=":tropical_drink:")
lstdrink=("cà phê trứng", "cà phê đen", "trà sữa", "sinh tố bơ", "milo dầm")
lstsugar=("đường trắng", "đường đen", "đường nâu", "đường vàng")
lsttoppings=("chocalate viên", "cốt dừa", "foam phô mai")
with st.form(key="td"):
    do_uong=st.selectbox(label="Chọn đồ uống", options=lstdrink)
    duong=st.selectbox(label="Chọn đường", options=lstsugar)
    mon_them=st.selectbox(label="Chọn món thêm", options=lsttoppings)
    so_luong=st.slider("Chọn số lượng đồ uống",min_value=1, max_value=5, value=0, step=1)
    tran_chau=st.checkbox("Thêm trân châu?")
    bill={"Loại nước uống: " : do_uong, "Loại đường: " : duong, "Loại toppings: " : mon_them, "Số lượng đồ uống: " : so_luong, "Thêm trân châu: " : tran_chau}
    gui=st.form_submit_button("Mua")
    if gui:
        st.balloons()
        for x,y in bill.items():
            st.write("Bạn đã mua")
            st.write(x,y)
in_hoa_don = st.checkbox("In hoá đơn")
if in_hoa_don:
    hoa_don=""
    for x in bill:
        hoa_don += str(x) + "" + str(bill[x]) + "\n"
    st.download_button("In hoá đơn", hoa_don)
import os
import streamlit as st
import pickle as pkl
import numpy as np


# streamlit run "C:\Users\Kislay Karan\PycharmProjects\Bondora_P2P\Loan_web_app.py"

#model1 = pkl.load(open('C:/Users/Kislay Karan/PycharmProjects/Bondora_P2P/static/pipeline_class2.pkl', 'rb'))
#model2 = pkl.load(open('C:/Users/Kislay Karan/PycharmProjects/Bondora_P2P/static/pipeline_reg2.pkl', 'rb'))

current_path = os.getcwd()

# getting the current path
# loading in the model to predict on the data  
class_pipe = os.path.join(current_path, 'static/pipeline_class2.pkl')

with open(class_pipe, 'rb') as pickle_in1:

    model1 = pkl.load(pickle_in1)

reg_pipe = os.path.join(current_path, 'static/pipeline_reg2.pkl')
    
with open(reg_pipe, 'rb') as pickle_in2:

    model2 = pkl.load(pickle_in2)
    

def predict_LoanStaus(input_data):
    
    prediction1=model1.predict(input_data)
    return int(prediction1)


def predict_emi_ela_proi(input_data):

    prediction2=model2.predict(input_data)
    prediction2 = prediction2.reshape([3, 1])
    m = np.array(prediction2)
    n =m.flatten()
    list(n)
    return (n)


def main():
    st.title("Loan Risk Predictor and Analyser ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">A BONDORA P2P PRODUCT </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Fill in the Borrower's Information :")
    
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
            
    with col1:
        BidsPortfolioManager = st.number_input("Bids Portfolio Manager", min_value=0.0)
    with col2:
        BidsApi = st.number_input("Bids Api", min_value=0.0)
    with col3:
        BidsManual = st.number_input("Bids Manual", min_value=0.0)
    with col4:
        Age = st.number_input("Age", min_value=0)
    with col5:
        AppliedAmount = st.number_input("Applied Amount", min_value=0.0)
    with col1:
        Interest = st.number_input("Interest", min_value=0.00)
    with col2:
        MonthlyPayment = st.number_input("Monthly Payment", min_value=0.00)
    with col3:
        IncomeTotal = st.number_input("Total Income", min_value=0.00)
    with col4:
        ExistingLiabilities = st.number_input("Existing Liabilities", min_value=0)
    with col5:
        RefinanceLiabilities = st.number_input("Refinance Liabilities", min_value=0)
    with col1:
        DebtToIncome = st.number_input("Debt To Income", min_value=0.0)
    with col2:
        FreeCash = st.number_input("Free Cash", min_value=0.0)
    with col3:
        PrincipalPaymentsMade = st.number_input("Principal Payments Made", min_value=0.0)
    with col4:
        InterestAndPenaltyPaymentsMade = st.number_input("Interest And Penalty Payments Made", min_value=0.0)
    with col5:
        PreviousRepaymentsBeforeLoan = st.number_input("Previous Repayments Before Loan", min_value=0.00)
    with col1:
        VerificationType = st.selectbox('Select VerificationType',['Income and expenses verified','Income unverified','Income verified','Income unverified,cross-referenced by phone','Not Set'])
    with col2:
        LanguageCode = st.selectbox('Select Language',['Estonian','Finnish','Spanish', 'Russian', 'English', 'Slovakian', 'German', 'Other'])
    with col3:
        Gender = st.selectbox('Select Gender',['Male', 'Female', 'Undefined'])
    with col4:
        Country = st.selectbox('Select Country',['EE','FI','ES','SK'])
    with col5:
        UseOfLoan = st.selectbox('Use Of Loan',['Not Set', 'Other', 'Home improvement', 'Loan consolidation', 'Vehicle', 'Business', 'Travel', 'Health', 'Education', 'Real estate', 'Purchase of machinery equipment','Other business' ,'Accounts receivable financing', 'Working capital financing', 'Acquisition of stocks', 'Acquisition of real estate', 'Acquisition of means of transport' ])
    with col1:
        Education = st.selectbox('Select Education',['Secondary education','Higher education', 'Vocational education', 'Basic education', 'Primary education', 'Not Present'])
    with col2:
        MaritalStatus = st.selectbox('Select Marital Status',['Not Specified', 'Single', 'Married', 'Cohabitant', 'Divorced', 'Widow' ])
    with col3:
        EmploymentStatus = st.selectbox('Select Employment Status',['Not present', 'Fully employed', 'Entrepreneur', 'Retiree', 'Self-employed', 'Partially employed'])
    with col4:
        EmploymentDurationCurrentEmployer = st.selectbox('Select Current Employment Duration',['TrialPeriod','UpTo1Year', 'UpTo2Years', 'UpTo3Years', 'UpTo4Years', 'UpTo5Years', 'MoreThan5Years','Other','Retiree'])
    with col5:
        OccupationArea = st.selectbox('Select Occupation Type',['Not present', 'Other', 'Retail and wholesale', 'Construction', 'Processing', 'Transport and warehousing', 'Healthcare and social help', 'Hospitality and catering', 'Info and telecom', 'Civil service & military', 'Education', 'Finance and insurance', 'Agriculture', 'forestry and fishing', 'Administrative', 'Energy', 'Art and entertainment', 'Research', 'Real-estate', 'Utilities', 'Mining'])
    with col1:
        HomeOwnershipType = st.selectbox('Select Home Ownership Type',['Owner','Tenant,pre-furnished property','Living with parents', 'Mortgage', 'Other', 'Joint ownership', 'Not specified', 'Joint tenant', 'Council house', 'Owner with encumbrance', 'Homeless'])
    with col2:
        Rating = st.selectbox('Enter Rating',[ 'AA', 'A', 'B', 'C', 'D', 'E', 'HR','F'])
    with col3:
        CreditScoreEsMicroL = st.selectbox('Enter Credit Score EsMicroL',['M', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10'])
    with col4:
        NewCreditCustomer = st.radio('New Credit Customer', ['True','False'],horizontal=True)
    with col5:
        Restructured = st.radio('Restructured', ['True','False'],horizontal=True)        

    result1 = ""
    result2 = ""

    default_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your Loan Status is Default</h2>
       </div>
    """
    notdefault_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your Loan Status is Not Default</h2>
       </div>
    """
    
    input=[BidsPortfolioManager, BidsApi, BidsManual, NewCreditCustomer,
        VerificationType, LanguageCode, Age, Gender, Country,
        AppliedAmount, Interest, MonthlyPayment, UseOfLoan, Education,
        MaritalStatus, EmploymentStatus,
        EmploymentDurationCurrentEmployer, OccupationArea,
        HomeOwnershipType, IncomeTotal, ExistingLiabilities,
        RefinanceLiabilities, DebtToIncome, FreeCash, Rating,
        Restructured, CreditScoreEsMicroL, PrincipalPaymentsMade,
        InterestAndPenaltyPaymentsMade, PreviousRepaymentsBeforeLoan]
    
            
    
    # changing the input_data to numpy array
    input1 =np.asarray(input)
   
    input_data = input1.reshape(1,-1)
    
    
    col1, col2= st.columns([1,1])
    
    
    with col1:
        if st.button("Loan Status"):
            result1 = predict_LoanStaus(input_data)
            if result1 == 0:
                st.success('Your Loan Status is Not Default')
                #st.markdown(notdefault_html, unsafe_allow_html=True)
            else:
                st.error('Your loan Status is Default')
                st.markdown(default_html, unsafe_allow_html=True)


    with col2:
        if st.button("Prediction"):
            result2 = predict_emi_ela_proi(input_data)
            a=float(result2[0])
            a=round(a,2)
            b=float(result2[1])
            b=round(b,2)
            c=float(result2[2])
            c=round(c,2)
            st.info("Preferred Equated Monthly Installment (EMI) is : € {}".format(a))
            st.info("Estimated Loan Amount (ELA) is : € {}".format(b))
            st.info("Possible Return On Investment (PROI) is : {} %".format(c))



if __name__=='__main__':
    main()

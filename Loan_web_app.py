import os
import streamlit as st
import pickle as pkl
import numpy as np


# streamlit run "C:\Users\Kislay Karan\PycharmProjects\Bondora_P2P\Loan_web_app.py"

current_path = os.getcwd()

# getting the current path
# loading in the model to predict on the data  
class_pipe = os.path.join(current_path, 'static\pipeline_class2.pickle')

with open(class_pipe, 'rb') as pickle_in1:

    model1 = pkl.load(pickle_in1)

class_reg = os.path.join(current_path, 'static\pipeline_reg2.pickle')
    
with open(class_reg, 'rb') as pickle_in2:

    model2 = pkl.load(pickle_in2)
    
# loading in the model to predict on the data  
#pickle_in1 = open('pipeline_class2.pkl','rb')  
#model1 = pkl.load(pickle_in1)

# loading in the model to predict on the data  
#pickle_in2 = open('pipeline_reg2.pkl','rb')  
#model2 = pkl.load(pickle_in2)

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
    <h2 style="color:white;text-align:center;">A BONDORA PRODUCT </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Fill in the Borrower's Information :")
    VerificationType = st.selectbox('Select VerificationType',['Income and expenses verified','Income unverified','Income verified','Income unverified,cross-referenced by phone','Not Set'])
    LanguageCode = st.selectbox('Select Language',['Estonian','Finnish','Spanish', 'Russian', 'English', 'Slovakian', 'German', 'Other'])
    Gender = st.selectbox('Select Gender',['Male', 'Female', 'Undefined'])
    Country = st.selectbox('Select Country',['EE','FI','ES','SK'])
    UseOfLoan = st.selectbox('UseOfLoan',['Not Set', 'Other', 'Home improvement', 'Loan consolidation', 'Vehicle', 'Business', 'Travel', 'Health', 'Education', 'Real estate', 'Purchase of machinery equipment','Other business' ,'Accounts receivable financing', 'Working capital financing', 'Acquisition of stocks', 'Acquisition of real estate', 'Acquisition of means of transport' ])
    Education = st.selectbox('Select Education',['Secondary education','Higher education', 'Vocational education', 'Basic education', 'Primary education', 'Not Present'])
    MaritalStatus = st.selectbox('Select Marital Status',['Not Specified', 'Single', 'Married', 'Cohabitant', 'Divorced', 'Widow' ])
    EmploymentStatus = st.selectbox('Select Employment Status',['Not present', 'Fully employed', 'Entrepreneur', 'Retiree', 'Self-employed', 'Partially employed'])
    EmploymentDurationCurrentEmployer = st.selectbox('Select Current Employment Duration',['TrialPeriod','UpTo1Year', 'UpTo2Years', 'UpTo3Years', 'UpTo4Years', 'UpTo5Years', 'MoreThan5Years','Other','Retiree'])
    OccupationArea = st.selectbox('Select Occupation Type',['Not present', 'Other', 'Retail and wholesale', 'Construction', 'Processing', 'Transport and warehousing', 'Healthcare and social help', 'Hospitality and catering', 'Info and telecom', 'Civil service & military', 'Education', 'Finance and insurance', 'Agriculture', 'forestry and fishing', 'Administrative', 'Energy', 'Art and entertainment', 'Research', 'Real-estate', 'Utilities', 'Mining'])
    HomeOwnershipType = st.selectbox('Select Home Ownership Type',['Owner','Tenant,pre-furnished property','Living with parents', 'Mortgage', 'Other', 'Joint ownership', 'Not specified', 'Joint tenant', 'Council house', 'Owner with encumbrance', 'Homeless'])
    Rating = st.selectbox('Enter Rating',[ 'AA', 'A', 'B', 'C', 'D', 'E', 'HR','F'])
    CreditScoreEsMicroL = st.selectbox('Enter Credit Score EsMicroL',['M', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10'])
    NewCreditCustomer = st.radio('New Credit Customer', ['True','False'])
    Restructured = st.radio('Restructured', ['True','False'])
    BidsPortfolioManager = st.number_input("Bids Portfolio Manager", min_value=0.0)
    BidsApi = st.number_input("Bids Api", min_value=0.0)
    BidsManual = st.number_input("Bids Manual", min_value=0.0)
    Age = st.number_input("Age", min_value=0)
    AppliedAmount = st.number_input("Applied Amount", min_value=0.0)
    Interest = st.number_input("Interest", min_value=0.00)
    MonthlyPayment = st.number_input("Monthly Payment", min_value=0.00)
    IncomeTotal = st.number_input("Total Income", min_value=0.00)
    ExistingLiabilities = st.number_input("Existing Liabilities", min_value=0)
    RefinanceLiabilities = st.number_input("Refinance Liabilities", min_value=0)
    DebtToIncome = st.number_input("Debt To Income", min_value=0.0)
    FreeCash = st.number_input("Free Cash", min_value=0.0)
    PrincipalPaymentsMade = st.number_input("Principal Payments Made", min_value=0.0)
    InterestAndPenaltyPaymentsMade = st.number_input("Interest And Penalty Payments Made", min_value=0.0)
    PreviousRepaymentsBeforeLoan = st.number_input("Previous Repayments Before Loan", min_value=0.00)
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
    
    
    
    
    if st.button("Loan Status"):
        result1 = predict_LoanStaus(input_data)
        if result1 == 0:
            st.success('Your loan Status is Not Default')
            st.markdown(notdefault_html, unsafe_allow_html=True)
        else:
            st.error('Your loan Status is Default')
            st.markdown(default_html, unsafe_allow_html=True)

    if st.button("Prediction"):
        result2 = predict_emi_ela_proi(input_data)
        a=float(result2[0])
        a=round(a,2)
        b=float(result2[1])
        b=round(b,2)
        c=float(result2[2])
        c=round(c,2)
        st.success("Preferred Equated Monthly Installment (EMI) is : € {}".format(a))
        st.success("Estimated Loan Amount (EMA) is : € {}".format(b))
        st.success("Preferred Return On Investment (PROI) is : {} %".format(c))


if __name__=='__main__':
    main()
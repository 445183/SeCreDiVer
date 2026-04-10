# # Se.Cre.Di.Ver :-
*Selective Credential Disclosure & Verification*

<br>
<br>
<br>

**-By** : *Aryan Kurkure*;
          *Devansh Masani*.

**-Pursuing** : *B.Tech in Data Science & Artificial Intelligence, IIT Roorkee*.

**-Date** : *10th April 2026*.

<br>
<br>
<br>

## -> Problem Statement :
   As far as real life usage of credentials is concerned, they are often exploited in terms of both against the person holding it and also may be by the person holding it as well.
<br>
<br>
#### How ?
1. An example to show how it can be possibly used against the holder is;
            Suppose the user wants to verify age, but has only access to Aadhaar card, then in that case to reveal his age he would have to reveal his Aadhaar card            as a whole which would be rather way more disclosing, as it would even tell about active address of the person and allows usage in many government websites           such as ration distribution etc.

3. When its exploited by the user;
            Suppose there to be present some digital certificate, or marks then by several online editing tools i can get those updated, in legal terms called as              tampering the data, which would cause issues in terms of consistency of data *(refers to data being unchanged in layman terms)*.

   One common place of actual realization would be the data leaks and tampering happening, or more commonly in daily life calls from companies you might of recently registered with and might have shared phone number just for otp verification, even highlighted in many movies.

<br>
<br>
<br>

## -> Solution :
   Now knowing the two main issues with credentials handling, we can say what we want to uphold is user's privacy along with not letting him/her to tamper the data or get it verified if so. So, is why the name of project is **Selective Credential Disclosure and Verification**;

   So, as far as privacy is concerned we would be achieving it via hashing *(In layman terms it deals with unique representation of any given data piece be it string, integer etc. into a secure 256 bits representation, in context to sha256 protocol being used in the project)* rest of the credential fields or parameters which the user doesn't want to reveal or are required by the authority which's verifying.

<br>
<br>

   Moving on to to the verification purposes, this is where it gets interesting and requires the most of the project's logic to jump in; we would be achieving this from two perspectives;
   1. If its actually issued by the institution being stated; 

         this would be taken care by **ECDSA** *(Elliptic Curve Digital Signing Algorithm)*, which in brief works over modular inverses, and arithmetic operations in 2D and different private keys being held by institutions which makes each institution which is issuing the cred. unique;
   
   2. If the data is consistent or no;

         by the concept of **Merkle trees** briefly, which would be bent on the fact of hashing the credentials originally for the uppermost layer or the leaves after which each adjacent leaf would be paired up and their strings' concatenation would be hashed to form the lower root node, we would be doing it iteratively even by pairing up the nodes until we are left with only one root, if you change any of the credential fields now, this would cause the lowermost or singular root to change by the principle of hashing being one-one function hence, effectively being a measure to check on tampering.

<br>
<br>
<br>

## -> Flow of the project :
   As identified earlier the project consists of 3 main pillars which would be having different levels of control over the credentials and how they are allowed to interact with them (all of those three would be having different separate tabs in the interface);
<br>
<br>
   1. ***Issuer*** - relates to the institution which would be creating the credentials, can possibly **create and issue** credentials with different fields in different people's name, identity would be safeguarded by the **unique private key** generated for them used in ECDSA ;
      
   2. ***Holder*** - as the name suggests, it allows for **searching for the credentials** and downloading a **disclosure file** which would provide the user with only the **fields he/she wants disclosed to be revealed** and rest all **field names would be mentioned but the values would be hashed**, furthermore the disclosure would contain the **adjacent leaves or root nodes for rebuilding the tree to get the lowermost root node for verification**.

   3. ***Verifier*** - Can **upload the disclosure files** of the candidate to check if its **valid or no by Merkle trees** and also **states the field values revealed in order to check if all required fields or parameters by the verifier are present or no**.

*All three would also be having the power to revoke the credentials which would be effectively used to revoke any credential if found malicious, either by the issuer or the verifier.*

<br>
<br>
<br>

## -> Table of Contents :
<br>
<br>
* streamlit interface explanation

1. Issuer page
2. Holder page
3. Verifier page

<br>
<br>
<br>

### ***** Streamlit explanation -

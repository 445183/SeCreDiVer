# Se.Cre.Di.Ver :-
Selective Credential Disclosure & Verification

**-By** : *Aryan Kurkure*;
          *Devansh Masani*.

**-Pursuing** : *B.Tech in Data Science & Artificial Intelligence*.

**-Date** : *10th April 2026*.

## Problem Statement -
   As far as real life usage of credentials is concerned, they are often exploited in terms of both against the person holding it and also may be by the person holding it as well.

### How ?
1. An example to show how it can be possibly used against the holder is;
            Suppose the user wants to verify age, but has only access to Aadhaar card, then in that case to reveal his age he would have to reveal his Aadhaar card            as a whole which would be rather way more disclosing, as it would even tell about active address of the person and allows usage in many government websites           such as ration distribution etc.

3. When its exploited by the user;
            Suppose there to be present some digital certificate, or marks then by several online editing tools i can get those updated, in legal terms called as              tampering the data, which would cause issues in terms of consistency of data *(refers to data being unchanged in layman terms)*.

   One common place of actual realization would be the data leaks and tampering happening, or more commonly in daily life calls from companies you might of recently registered with and might have shared phone number just for otp verification, even highlighted in many movies.

## Solution -
   Now knowing the two main issues with credentials handling, we can say what we want to uphold is user's privacy along with not letting him/her to tamper the data or get it verified if so. So, is why the name of project is **Selective Credential Disclosure and Verification**;

   So, as far as privacy is concerned we would be achieving it via hashing *(In layman terms it deals with unique representation of any given data piece be it string, integer etc. into a secure 256 bits representation, in context to sha256 protocol being used in the project)* rest of the credential fields or parameters which the user doesn't want to reveal or are required by the authority which's verifying.
   Moving on to to the verification purposes, this is where it gets interesting and requires the most of the project's logic to jump in; we would be achieving this from two perspectives;
   1. If its actually issued by the institution being stated;
   2. If the data is consistent or no.

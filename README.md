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
# streamlit interface explanation

1. Issuer page
2. Holder page
3. Verifier page

<br>
<br>
<br>

### # Streamlit explanation -
   It consists nothing to the logical essence of the project but to the interface part, and enables locally hosting the project for better experience of how the project would look like in case its adapted in the ongoing digital era.
   Some of the importantly used functions from the streamlit library after importing it via *import streamlit as sl* are :
   1. **sl.set_page_config()** -> It takes in parameters like *page_title, page_icon and layout* which help customize the appearance;
   2. **sl.tabs()** -> It helps create several pages of interaction within the same page of the interface, it takes in list of names of the tabs which we want to create and returns the same number of tabs which can be unwrapped as, tab1, tab2,... =sl.tabs(["..", "..", ...]);
   3. **sl.session_state** -> Undeniably its the most important part of the project as, streamlit hosted interface has the issue of reloading everytime there's interaction between the interface and the user, so in order to save the inputs etc. between those updations we use sl.session_state;
         * Eg; sl.session_state.authority is used to store the name of the institution; further more its important to check if some object like 'authority' exists within sl.session_state we check it using membership operators like *"in"* !
   4. Presentation of data -> *(all take in strings as input)*
      * **sl.title()**;
      * **sl.header()**;
      * **sl.subheader()**;
      * **sl.write()**;
      * **sl.json()**; *unlike others this also takes dict, list as inputs along with json formatted string as input, and unlike others which only allow showing text data, this one allows for showing json data.*

<br>

*sl.divider() is used to create lines in order to partition between two i/o structures of interface*
<br>

   5. Different inputs method ->
      * **sl.text_input()** ; provide one main compulsory string for asking the user about what he/she is supposed to enter and *placeholder='..'* which is like an sample input;
      * **sl.radio()** ; provide a list of possible options in strings out of which one can be selected and would be presented as the returned value;
      * **sl.file_uploader()** ; one main string stating what is expected to be uploaded and then keyword argument *type=[..]* which asks for the data type of files, in our case json.
   6. Showing status of operations in interface -> *(as name suggests, and all take string as message to be diplayed)*
      * **sl.success()**;
      * **sl.warning()**;
      * **sl.error()**.
   7. To trigger any operation, we use **sl.button()**.

<br>
<br>

### **I. Issuer page -**
Allows the issuer to;

   1. **Register an institution** by entering its name and clicking **SUBMIT**. Upon submission, an **IssuerAuthority** object is created and stored in **sl.session_state.authority**. This object internally calls **genKeys()** which generates a cryptographic keypair for the institution consisting of a *private key* and a *public key*, the mechanism behind which is explained ahead.

   2. **Add credential fields** one by one, each having a name, a type *(str, int, float, bool)* and a value entered through type-specific widgets. Each field is accumulated as a dictionary entry in **sl.session_state.fields_buffer** until issuance.

   3. **Issue a credential** by providing the holder's name and validity days, after which **issueCred()** is called. This internally builds a Merkle tree over the fields, signs the Merkle root with ECDSA, and packages everything into a credential dictionary which is saved to the local wallet directory via **save_cred()**.

   4. **View the issued credential** displayed via **sl.json()** directly beneath the issue section, showing all fields, the Merkle root, the ECDSA signature, timestamps, and the institution's public key.

<br>

#### Cryptographic operations triggered by the Issuer page :

<br>

##### a) Key generation — **genKeys()** in **core/ecdsa.py** :
   When the institution is registered, **genKeys()** is called. It picks a cryptographically secure random integer *d* in the range [1, n-1] as the **private key** using **secrets.randbelow()**. The **public key** Q is then derived as *d × G* where G is the generator point of the secp256k1 elliptic curve — a fixed standardised point agreed upon universally. This multiplication is performed by **scalMul()** in **core/ec.py** using the *double-and-add* algorithm, which is essentially repeated point addition on the curve but done efficiently by processing the binary representation of d.

   The security of this rests on the **Elliptic Curve Discrete Logarithm Problem** — given Q and G, finding d is computationally infeasible even with the most powerful hardware, because scalar multiplication on an elliptic curve is a one-way operation. The private key never leaves **sl.session_state.authority**; the public key is embedded into every issued credential via **xyTob64()** which serialises the EC point coordinates to a base64url string.

<br>

##### b) Field encoding — **encode_field()** in **core/fieldEnc.py** :
   Before any field value can be hashed, it must be converted to bytes in a consistent and unambiguous way. **encode_field()** takes the field name and its Python value and produces a UTF-8 encoded byte string of the format **name:type:value**. For example, a field named *degree* with value *BSc CS* becomes **b'degree:str:BSc CS'**. The type label is derived from **type(value).__name__** and is included in the encoding so that two fields with the same value but different types — such as integer 1 and boolean True — never produce the same byte string and therefore never collide in the Merkle tree.

<br>

##### c) Merkle tree construction — **mkTree()** in **core/merkle.py** :
   After all field pairs are collected, **mkTree()** is called with the list of *(name, value)* tuples. It works in two stages:

   - **Leaf layer** : each field is passed through **encode_field()** and then **hash_leaf()** which applies **sha256** to produce a 32-byte leaf hash. All leaf hashes form the bottom layer of the tree.
   - **Upward pairing** : adjacent leaves are paired and their concatenation is hashed using **hash_node()** to produce the next level. If the count at any level is odd, the last node is paired with itself. This repeats until only one hash remains — the **Merkle root**.

   The entire tree is stored as a list of lists of bytes, serialised to hex strings via **bytToStr()** before being stored in the credential dictionary, since raw bytes cannot be written to a JSON file.

   The significance of this structure is that changing any single field value changes its leaf hash, which cascades upward changing every ancestor hash, and ultimately changes the root. Since the root is signed by the issuer, any such change invalidates the signature and is immediately detectable during verification.

<br>

##### d) ECDSA signing — **sign()** in **core/ecdsa.py** :
   Once the Merkle root is obtained as bytes, **sign(root, self.priv_k)** is called. The signing process works as follows:

   1. The root bytes are hashed with **sha256** and converted to an integer *z* modulo *n*, producing the message digest.
   2. A fresh random nonce *k* is chosen from [1, n-1] via **secrets.randbelow()**.
   3. The point *R = k × G* is computed via **scalMul()**. The x-coordinate of R modulo n gives the signature component *r*.
   4. The signature component *s* is computed as *modinv(k, n) × (z + r × d) mod n* where *d* is the private key.
   5. The pair *(r, s)* is the signature. It is serialised to a dictionary of 64-character hex strings via **rsToDict()** for JSON storage.

   The nonce *k* is discarded immediately after use. It must never be reused — reusing k across two signatures mathematically leaks the private key. The final credential dictionary contains this serialised signature alongside the root hex, the public key, all fields with their types, the serialised Merkle levels, and the issuance and expiry timestamps.

<br>
<br>

### **II. Holder page -**
Allows the holder to;

   1. **Find credentials by name** — the holder enters their name and clicks **FIND MY CREDENTIALS**. The system calls **list_cred()** which reads all **.json** filenames from the wallet directory, then **load_cred()** on each, filtering those where **cred['holder']** matches the entered name. Matching credential IDs are stored in **sl.session_state.my_creds**.

   2. **Load or delete a credential** — from a radio selector showing all matching credential IDs, the holder can load a specific credential into **sl.session_state.last_cred** or delete it from disk via **del_cred()**.

   3. **Select an institution** — if multiple credentials exist for the same holder name from different institutions, a radio selector shows the issuer names and the corresponding credential is set as **sl.session_state.last_cred**.

   4. **Select fields to reveal** — field names from the loaded credential are displayed. The holder enters the indices of the fields they wish to reveal as space-separated integers, which are mapped to field names internally.

   5. **Create a disclosure** — clicking **SUBMIT QUERY** calls **showCred()** which rebuilds the Merkle tree from the stored fields, generates proof paths for revealed fields, and computes leaf hashes for hidden fields. The resulting disclosure dictionary is stored in **sl.session_state.last_disc** and offered for download as a JSON file via **sl.download_button()**.

<br>

#### Cryptographic operations triggered by the Holder page :

<br>

##### a) Merkle proof generation — **getProof()** in **core/merkle.py** :
   For each field the holder chooses to reveal, **getProof(tree, index)** generates the **sibling hash path** from that leaf up to the root. At each level of the tree, it identifies the sibling of the current node — the adjacent hash that was paired with it — and records whether that sibling sits to the left or right. This *(sibling_hash, side)* pair is collected for every level, giving a list of pairs that together allow anyone to independently recompute the root from just the leaf value.

   The proof path is what makes selective disclosure possible. The verifier can confirm a single field is genuine without needing to see any other field, because the proof path provides exactly the information needed to reconstruct the root — no more, no less.

<br>

##### b) Hidden field hashing — **hash_leaf()** in **core/hashing.py** :
   For every field the holder does **not** wish to reveal, **showCred()** takes that field's precomputed leaf hash directly from the tree's bottom layer — **ht[0][i].hex()** — and includes it in the disclosure under the **hidden** dictionary. The verifier receives these hashes but cannot reverse them to find the original values, since **sha256** is a one-way function. Yet the verifier still needs them to recompute the Merkle root when verifying revealed fields, because every leaf — revealed or hidden — contributes to the root computation.

   This is the cryptographic mechanism behind privacy in this system. Hidden fields are not absent from the disclosure — they are present as hash commitments. Their existence is acknowledged but their content is protected.

<br>

##### c) Disclosure packet structure :
   The disclosure dictionary produced by **showCred()** contains:
   - **issuer_public_key** — the base64url serialised EC point of the issuing institution.
   - **root** — the Merkle root hex string copied from the credential.
   - **signature** — the serialised ECDSA signature *(r, s)* copied from the credential.
   - **issued_at** and **expires_at** — ISO 8601 UTC timestamp strings.
   - **revealed** — a list of dictionaries, one per revealed field, each containing the field name, value, type label, leaf index, and Merkle proof path as a list of **[hex_string, side]** pairs.
   - **hidden** — a dictionary mapping each hidden field name to its leaf hash hex string.

   Every value in this dictionary is JSON serialisable, so **json.dumps()** called by **sl.download_button()** never raises a **TypeError**.

<br>
<br>

### **III. Verifier page -**
Allows the verifier to;

   1. **Upload a disclosure file** — the verifier uploads the **.json** disclosure file produced by the holder via **sl.file_uploader()**. The file bytes are read with **.getvalue().decode()** and parsed with **json.loads()**. The parsed dictionary is stored in **sl.session_state.disc**. If the JSON is malformed, an error is shown and no further action is taken.

   2. **Verify the disclosure** — clicking **VERIFY** calls **verifyDisc(disc)** from **verifier/verify.py**. This function runs four sequential checks and returns a *(bool, reason_string)* tuple. If valid, the revealed fields and their values are displayed along with the issuance and expiry timestamps and a list of hidden field names. If invalid, the exact reason is shown via **sl.error()**.

   3. **Revoke a credential** — an expander at the bottom of the page allows any actor to enter a credential root hex and call **revCred()** which appends it to the revocation registry file. Any future verification of that credential will fail at Check 4.

<br>

#### Cryptographic operations triggered by the Verifier page :

<br>

##### a) Check 1 — Expiry :
   **datetime.fromisoformat(disc['expires_at'])** parses the expiry timestamp stored in the disclosure. It is compared against **datetime.now(timezone.utc)**. If the current time is past the expiry, the function immediately returns **(False, 'Credential has expired !')**. This check requires no cryptography — it is a straightforward timestamp comparison — but it is placed first because it is the cheapest check to run and eliminates stale credentials before any heavier computation begins.

<br>

##### b) Check 2 — Merkle proof verification — **verifyProof()** in **core/merkle.py** :
   For each item in **disc['revealed']**, the verifier reconstructs the Merkle root from that single field and its proof path. The process is:

   1. The revealed field's name and value are passed to **encode_field()** and then **hash_leaf()** to reproduce the original leaf hash.
   2. The proof path is iterated. At each step, the current hash and its sibling are combined using **hash_node()**. The **side** value determines the order — if the sibling is on the left, it goes first; if on the right, the current hash goes first.
   3. After all levels are processed, the final computed hash must equal **bytes.fromhex(disc['root'])**.

   If any revealed field's computed root does not match the stored root, verification fails with **'Invalid proof for consistency !'**. This proves that either the field value was tampered with after issuance, or the proof path itself was falsified.

<br>

##### c) Check 3 — ECDSA signature verification — **verify()** in **core/ecdsa.p** :
   The verifier recovers the issuer's public key Q via **xyFromb64(disc['issuer_public_key'])** and the signature *(r, s)* via **dictToRS(disc['signature'])**. The root is converted to bytes via **bytes.fromhex(disc['root'])**. Then **verify(root_bytes, sig, Q)** is called:

   1. The root bytes are hashed and converted to integer *z* exactly as was done during signing.
   2. The modular inverse of *s* is computed. Then *u1 = modinv(s, n) × z mod n* and *u2 = modinv(s, n) × r mod n* are derived.
   3. The point *u1 × G + u2 × Q* is computed using **scalMul()** and **pointAdd()**.
   4. If the x-coordinate of this point modulo *n* equals *r*, the signature is valid.

   This works because the verification equation expands mathematically to reproduce the original nonce point only if the signer held the private key *d*. Without *d*, it is impossible to produce *(r, s)* values that satisfy this equation. A valid result here proves the credential was genuinely signed by the institution whose public key is embedded in the disclosure.

   If verification fails, the function returns **(False, 'Not authenticated by the institution !')**.

<br>

##### d) Check 4 — Revocation — **isRev()** in **issuer/revocation.py** :
   **isRev(root_hex)** opens **revo_reg.json** from the issuer's revocation registry directory and checks whether **disc['root']** appears in the **revoked** list. If it does, the credential has been explicitly invalidated by the issuer and verification fails with **'The credentials have been revoked by the institution !'**. If the registry file does not exist, no credentials have been revoked and this check passes.

   Revocation provides the issuer with the ability to invalidate credentials after issuance — for instance if a degree is rescinded, an employee is terminated, or a document is reported stolen. Since the Merkle root uniquely identifies every credential, adding it to the revocation list is both simple and unambiguous.

<br>
<br>
<br>

## -> How to run :

   1. Download the repository and navigate to the project directory *(The main folder, SeCreDiVer)* in command prompt.
   2. Install dependencies via ***pip install streamlit, hashlib, json***.
   3. Run the Streamlit app via **streamlit run app.py** command in command prompt ***after step 1.***.
   4. The app opens in the browser at *http://localhost:8501*.

<br>
<br>
<br>

## -> Project structure :

*SeCreDiVer/
|
|-- core/
|   |-- ec.py           elliptic curve operations and secp256k1 constants
|   |-- ecdsa.py        key generation, signing, verification
|   |-- fieldArith.py   modular inverse and primality
|   |-- fieldEnc.py     field value encoding to bytes
|   |-- hashing.py      sha256 wrappers for leaf and node hashing
|   |-- merkle.py       Merkle tree build, proof, verify, serialisation
|
|-- issuer/
|   |-- authority.py    IssuerAuthority class — issuance pipeline
|   |-- revocation.py   revocation registry read and write
|
|-- holder/
|   |-- wallet.py       credential storage and retrieval
|   |-- disclosure.py   selective disclosure packet creation
|
|-- verifier/
|   |-- verify.py       four-check verification pipeline
|
|-- app.py              Streamlit UI — Issuer, Owner, Verification tabs*

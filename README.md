# $\color{#FFD700}{\text{ Se.Cre.Di.Ver}}$
## *Selective Credential Disclosure & Verification*
<br>

$\color{#FF0000}{\text{To run the code, know the folder structure or know the topics used refer to the instructions at the last}}$
<br>
<br>
<br>

**-By** : *Aryan Kurkure*;  25125011      
          *Devansh Masani*.  25125011   

**-Pursuing** : *B.Tech in Data Science & Artificial Intelligence, IIT Roorkee*.

**-Date** : *10th April 2026*.

<br>
<br>
<br>

## $\color{#FFD700}{\text{-> Problem Statement :}}$

In our daily lives, we are constantly asked to "prove" who we are. Whether it's applying for a job, entering a building, or registering for a website, we face a broken "Privacy vs. Trust" paradox. To gain an institution's trust, we are currently forced to sacrifice our personal privacy.


### **1. The "Aadhaar" Over-Disclosure (The Privacy Leak)**
Think about the last time you used your Aadhaar card just to verify your age.
* To show you are "Over 18," you end up handing over a document that contains your permanent home address, your father's name, and your unique biometric ID.
* This is a massive over-disclosure of your **PII (Personally Identifiable Information)**.
* Once that data is out there, you lose control; it can be used to track you across government websites or shared with third parties without you ever knowing.

### **2. The "Photoshop" Fraud (The Trust Gap)**
Institutions are struggling with a lack of **Data Integrity**.
* Today, anyone with basic photo-editing skills can "update" their cgpa or change a date on a PDF certificate.
* Because standard digital documents have no built-in way to prove they haven't been changed since they were issued, tampering has become a major legal and security headache.

### **3. The "FAKE" Credential & The Waiting Game (Delay of Verific. & Revocation)**
Verifying or "taking back" a credential is currently a slow and a manual nightmare.
* **The Phone Call Loop**: If an employer wants to be 100% sure a degree is real, they often have to manually contact the University (the Issuer) via email or phone, creating high-latency verification that wastes days of time.
* **The Revocation Problem**: If a degree is rescinded or an ID card is reported stolen, it stays valid forever in the current system because there is no way to instantly tell every verifier that it has been cancelled.
* Without a real-time **Revocation Registry**, these "FAKE Credentials" continue to be used for fraud.

### **4. The Spam Call Reality (Data Correlation)**
We’ve all experienced it: you share your phone number for a simple "OTP verification," and two days later, you’re flooded with spam calls from companies you’ve never heard of.
* Every time we share a centralized ID, we leave a digital footprint that companies use to track and profile us.
* These data leaks and the constant "selling" of our contact info have turned a simple verification step into a lifelong privacy risk.



<br>
<br>
<br>

## $\color{#FFD700}{\text{-> Solution :}}$

The goal of **SeCreDiVer** is to flip the "Privacy vs. Trust" paradox on its head. We provide a decentralized framework where a user can prove their identity with mathematical certainty without ever surrendering their personal privacy. 

Our solution is built on four cryptographic pillars:

### **1. Privacy through Selective Disclosure (SHA-256 Hashing)**
To solve the "Aadhaar Problem," we implement **Selective Disclosure**. 
* **The Logic**: Instead of sharing raw data for every field, the user provides a **SHA-256 hash** for sensitive information they wish to hide. 
* Think of this as a unique **digital fingerprint**. The Verifier knows the fingerprint represents a specific, valid data point, but because hashing is a "one-way" function, they cannot reverse-engineer it to see your actual home address or phone number.

### **2. Integrity through Merkle Trees (The Digital Seal)**
To stop someone from simply editing their marks on a digital certificate, we utilize **Merkle Trees**. 
* Every field is hashed into the "leaves" of a mathematical tree, which leads up to a single **Merkle Root**. 
* This Root acts like a high-tech wax seal. If a user tries to change even a single character in their credential, the resulting Root would change entirely. By recomputing the tree, the Verifier gets instant proof of **Data Integrity**.

### **3. Authenticity through ECDSA (Ending the "Phone Call" Loop)**
To remove the need for manual institutional verification, we use the **Elliptic Curve Digital Signing Algorithm (ECDSA)**.
* **Instant Trust**: Every institution (the Issuer) signs the Merkle Root with a unique **Private Key**. 
* The Verifier uses the institution’s **Public Key** to authenticate this signature in milliseconds. This eliminates **Verification Latency**—there is no need to call the college or wait for an email to confirm if a degree is real.

### **4. Real-Time Revocation (The Mathematical Kill-Switch)**
Finally, we handle the issue of stolen or rescinded IDs through a **Revocation Registry**. 
* Even if a document is mathematically perfect, the Verifier’s final check is against a digital "blacklist" of Merkle Roots. 
* This ensures that if a college has "taken back" or **revoked** a credential, it cannot be used for fraud. It effectively kills "zombie" certificates before they can be exploited.

<br>
<br>
---

## $\color{#FFD700}{\text{-> Project Flow :}}$
The **SeCreDiVer** system follows a **modular 5-tier pipeline** designed for high security and user privacy. By separating the logic into specific packages, we ensure that the mathematical "Trust Engine" is independent of the user interface.

1. **Mathematical Foundation (`core/`)**: The core engine handling **Elliptic Curve arithmetic** (`ec.py`) and **Merkle Tree generation** (`merkle.py`). This layer provides the cryptographic primitives for identity and data integrity.
<br>

2. **Institutional Issuance (`issuer/`)**: The Authority module where credentials are created and signed. It also maintains a real-time **Revocation Registry** (`revocation.py`) to instantly invalidate compromised or rescinded documents.
<br>

3. **Privacy & Selective Disclosure (`holder/`)**: The user’s digital wallet. Using `disclosure.py`, the user can hide sensitive fields (like **Caste**, **Address**, or **Phone Number**) by replacing them with **SHA-256 hashes**.
<br>

4. **The 4-Step Verification Pipeline (`verifier/`)**: A comprehensive audit that recomputes the Merkle Root to detect **tampering**, verifies the **ECDSA Signature** for authenticity, and checks the document’s expiry and revocation status.
<br>

5. **Integration & Interface (`app.py`)**: The orchestration layer. Using **Streamlit**, this file integrates all back-end modules into a real-time interactive dashboard, allowing for a seamless demonstration of the Issuer, Holder, and Verifier roles.
<br>

![Project Flow Diagram](assets/merkle_tree.png)


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
   - **Downward pairing** : adjacent leaves are paired and their concatenation is hashed using **hash_node()** to produce the next level. If the count at any level is odd, the last node is paired with itself. This repeats until only one hash remains — the **Merkle root**.

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
   For every field the holder does **not** wish to reveal, **showCred()** takes that field's precomputed leaf hash directly from the tree's top layer — **ht[0][i].hex()** — and includes it in the disclosure under the **hidden** dictionary. The verifier receives these hashes but cannot reverse them to find the original values, since **sha256** is a one-way function. Yet the verifier still needs them to recompute the Merkle root when verifying revealed fields, because every leaf — revealed or hidden — contributes to the root computation.

   This is the cryptographic mechanism behind privacy in this system. Hidden fields are not absent from the disclosure — they are present as hash commitments. Their **existence is acknowledged but their content is protected**.

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

   If any revealed field's computed root does not match the stored root, verification fails with **'Invalid proof for consistency !'**. This proves that either the field value was tampered with after issuance, or the proof path itself was wrong.

<br>

##### c) Check 3 — ECDSA signature verification — **verify()** in **core/ecdsa.py** :
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

## $\color{#FFD700}{\text{-> Application Domains :}}$

Our project is industry-agnostic. By swapping data fields, it serves any sector requiring **"Trust without Over-exposure"**:

* **Fair Recruitment & Social Equity:** Selectively hiding sensitive fields like **Caste** or **Religion** on certificates during interview rounds. This ensures merit-based hiring and eliminates unconscious bias while the system still cryptographically proves the degree is genuine.
* **Healthcare:** Proving **"Vaccination Status"** for travel without revealing a full medical history.
* **E-Governance:** Proving **"Residency"** for subsidies without sharing phone numbers or age to prevent tracking.

---

## $\color{#FFD700}{\text{-> Future Expansion :}}$

Built as a foundation for global identity standards, the project is ready for:

* **Zero-Knowledge Proofs (ZKP):** we aim if the equality: ***sG = R+cY*** holds where ***R = r * G, Y = d * G and s=(r + c * d)mod(n)***, *(where G is the generator point)* is provided to the verification institution by the holder of the private key d, hence without even revealing d to the verifier we can prove that holder knows d for some random message *c*, common to both.

###### Thereby this is a possible way of verification of credentials which the user wants to disclose without the verifier ever seeing them, which for now are being totally revealed !

* **isPrime() :** for now the modular operations, both of numbers and of the elliptic curve points are happening with respect to fixed primes as moduli however to make the project's primes dynamic; we can possibly generate over own primes and also to avoid the **root(n)** time complexity by avoiding the standard primality test by using, *Miller-Rabin test*; which is based on extension of the ***Fermat's little theorem (if, p is prime then a^(p-1) is congreunt to 1 mod p)*** which strictly requires ***a^(q * (2^(e))) to be either -1 or 1 mod p where q * (2^(e)) are proper divisors of p-1*** !, hence we check this condition for sufficiently large numbers of random values of ***a->[2,p-2]*** and if it satisfies then the number can be said to be prime!!

###### NOTE: For further clarifications we have provided the implementation of those functions in zkp folder and fieldArith.py respectively
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
<br>
|
<br>
|-- core/
<br>
|   |-- ec.py           elliptic curve operations and secp256k1 constants
<br>
|   |-- ecdsa.py        key generation, signing, verification
<br>
|   |-- fieldArith.py   modular inverse and primality
<br>
|   |-- fieldEnc.py     field value encoding to bytes
<br>
|   |-- hashing.py      sha256 wrappers for leaf and node hashing
<br>
|   |-- merkle.py       Merkle tree build, proof, verify, serialisation
<br>
|
<br>
|-- issuer/
<br>
|   |-- authority.py    IssuerAuthority class — issuance pipeline
<br>
|   |-- revocation.py   revocation registry read and write
<br>
|
<br>
|-- holder/
<br>
|   |-- wallet.py       credential storage and retrieval
<br>
|   |-- disclosure.py   selective disclosure packet creation
<br>
|
<br>
|-- verifier/
<br>
|   |-- verify.py       four-check verification pipeline
<br>
|
<br>
|-- app.py              Streamlit UI — Issuer, Owner, Verification tabs*

<br>
<br>
<br>

#### TOPICS used :-
1. **LISTS OPERATIONS AND COMPREHENSION**, heavily used in merkle trees
2. **JSON and DICT** data structures used for project and json files interaction for reading, checking of the files are empty etc.
3. **HASHING concept is derived from DICT's** method of storing data for O(1) look up time, again used heavily in merkle tress
4. **MATHEMATICS IN PY** *and related libraries like gmpy2* for fast calculations, modular arithmetic etc.
5. **CLASSES** for maintaining issuer objects in the issuer panel
6. **DATA TYPES AND EXPLICIT TYPING** in python and inferring them from variables to ensure **json serialability**; ie, the json files can't hold all data types which might cause data loss, so appropriately the data-type is changed by **TYPE CASTING**
7. **KEYWORD ARGUMENTS** to pass on multiple parameters as field values while creating credentials.
8. **STREAMLIT** based user interaction panel development and local hosting.

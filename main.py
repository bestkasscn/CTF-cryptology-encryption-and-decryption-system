from Crypto.Util.number import *
import gmpy2
from xenny.ctf.crypto.modern.asymmetric.rsa import same_module

e1 = 65537
e2 = 65539
c1 = 0xab287887ee1ff1649414f4475858ba76b36161c8945c600b32eb7b20c2572350b64d217963e44be747a30a27a7003549797fb54cc34ea928a917ad8d9e94435761ddbf251b1221c896513716833b7c6772ed8c4a1f9c062c32727ecc46c45f84a2b2252619b33ba1146d0035a92f5fdb4b354438d7507bcd38c4316221cce1130e3bd9c28ea57648c3373662da8cf0d3051a26d326f59f8a81afd4bce6b2ddc1b06af177e2b7af9be48ac4d82b7a49b2f6ec06ead0b3fb5b14e27a61530639af3398b93a85b0fb618d4de262c9915d616a836fe15d1885a17ab0b088d87a9838eb999e4c6ab518e23159fb37267d3016bec866eb23302f6d6fb3478ce8b77121
c2 = 0x7da8f28261a4018a6babaee06edba7536101326f802f7af9e7d9a115d852b0d1ed71d9a68a294ec48851e5d40c10c489be5622f3b862000fe9b15fa3bcf933b98eef7fa028111e485bd6ce19a798c721fd5268d01085bcabb533a8df73cefd245500bba80b850c92a269f8e547fde0738941e491933fde84124b79ed75166a278fa112edf40336660bb1abf02eb34b1d21e054599f658677c7042eea0aa8dcc343040f7cfe2d713291b41b25f2022f812d0994a3668f0761ff6e6776af60d7e8e97772c354d5e02a0c0eb5a04d768143eee49f1c8abf0760ea8de99d82b084eb4101f36c01910529ed2d5904a8dee767e207f4a5a4f43a4ab6a134a6fa97b816
n = 0xd7e5039b7606ecbd0866a0a6aa3307ec5015fb84ca81a16e6e0aa02cc91612861bd0f395e201e4fd92cdf9366f609fe7d90de8aee04f008e85bcad9fb27f9261399f06c4b785ee6aa56d5dd2b8a7ce81b235faafc192291a3bc546be000a7a7a92d62cd8da3923f7cb78f8a353d383cf4447aeea918ee8d36a2167187e76cde62722a2eda318e798575df75f4284abc9877ba41b6b50ce6474768044d7d8bd7c19aefee3064037ff2cfd6c6741a26ba05698568cb3a226e9e3668a258da4bbc8dfb12cd510b676f3bfa0646dc7bcaf9fce2ac3b538094fad68180f4bfd62470e19446451ad6632a748633e075f6f471a26151739a3a53d6b8f86461d8ac55587
m = same_module.attack(n, e1, e2, c1, c2)
print(long_to_bytes(m))

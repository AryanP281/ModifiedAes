#include <cryptlib.h>

#include <chacha.h>

#include <iostream>



int main()

{

    using namespace CryptoPP;//crypto++ library namespace

    ChaChaTLS::Encryption ce; // we create an encryption object

    std::cout << "# KEY LENGTH: " << ce.DefaultKeyLength() << std::endl;

    std::cout << "# MINIMUM KEY LENGTH: " << ce.MinKeyLength () << std::endl;

    std::cout << "# MAXIMUM KEY LENGTH: " << ce.MaxKeyLength () << std::endl;

    std::cout << "# IV SIZE: " << ce.IVSize() << std::endl;

    return 0;

}
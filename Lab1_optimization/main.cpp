#include <iostream>
#include <vector>
#include <cmath>
#include <Eigen/Dense>
#include <chrono>
#include <random>

Eigen::MatrixXd f(const Eigen::VectorXd& x, const Eigen::MatrixXd& A, const Eigen::VectorXd& b) {
    Eigen::MatrixXd xt = x.transpose();
    Eigen::MatrixXd bt = b.transpose();
    return 0.5 * xt * A * x + bt * x;
}

Eigen::VectorXd f_dif(const Eigen::VectorXd& x, const Eigen::MatrixXd& A, const Eigen::VectorXd& b) {
    return A * x + b;
}

Eigen::MatrixXd gen_matrix( int dim) {
    Eigen::MatrixXd random_matrix(dim,dim) ;
//    std::minstd_rand random (std::chrono::system_clock::now().time_since_epoch().count());
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(1.0000000, 15.0000000);


    for(int i = 0; i < dim; i++)
        for(int j = 0; j < dim; j++)
            (i == j) ? (random_matrix(j,i) = dis(gen)) : 0;

    Eigen::MatrixXd A(dim,dim);

    for(int i = 0; i < dim; i++)
        for(int j = 0; j < dim; j++)
            A(j,i) = dis(gen);


    random_matrix = A * random_matrix * A.transpose();
    return  random_matrix;
}

Eigen::VectorXd gen_vec(int dim) {
    Eigen::VectorXd A(dim);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(1.0000000, 15.0000000);

    for(int i = 0; i < dim ; i++) {
        A(i) = dis(gen);
    }

    return A;
}


Eigen::VectorXd gradient(const Eigen::VectorXd& x, const Eigen::MatrixXd& A, const Eigen::VectorXd& b) {
    return x - 1e-4 * f_dif(x, A, b);
}



void calculate_gradient(const Eigen::VectorXd x, const Eigen::MatrixXd& A, const Eigen::VectorXd& b,
                        std::vector<Eigen::VectorXd> list_of_x, int& count, Eigen::MatrixXd&M ) {

   list_of_x.push_back(x);
   list_of_x.push_back(gradient(x,A,b));

   double norm = (list_of_x[1] - list_of_x[0]).norm();

    while(norm > 1e-6) {
        list_of_x.push_back(gradient(list_of_x[count], A, b));
//        std::cout<<"this is the  "<< count<<" iterator"<<std::endl;
//        std::cout<<list_of_x[count]<<std::endl;
//        std::cout<<"this is f(x) at x["<<count<<"] "<<f(list_of_x[count],A,b)<<std::endl;
        count++;
        norm = (list_of_x[count] - list_of_x[count - 1]).norm();
    }
    std::cout<<"m/4: "<<count/4<<std::endl<<"f(m/4) = "<<f(list_of_x[count],A,b)<<std::endl<<"vector m/4= "<<std::endl<<list_of_x[count]<<std::endl;
    std::cout<<"m/2: "<<count/2<<std::endl<<"f(m/2) = "<<f(list_of_x[count],A,b)<<std::endl<<"vector m/2= "<<std::endl<<list_of_x[count]<<std::endl;
    std::cout<<"3m/4: "<<(3*count)/4<<std::endl<<"f(3m/2) = "<<f(list_of_x[count],A,b)<<std::endl<<"vector 3m/2= "<<std::endl<<list_of_x[count]<<std::endl;
    std::cout<<"m: "<<count<<std::endl<<"f(m) = "<<f(list_of_x[count],A,b)<<std::endl<<"vector m= "<<std::endl<<list_of_x[count]<<std::endl;



}


int main() {
    int dim = 6;
//    Eigen::MatrixXd A = gen_matrix(dim);
//    Eigen::VectorXd x = gen_vec(dim);
//    Eigen::VectorXd b = gen_vec(dim);
    Eigen::MatrixXd A(6, 6);
    A << 1898.24, 2676.7, 1984.5, 2523.34, 2627.48, 2254.82,
            2676.7, 4962.88, 3751.33, 2908.49, 4348.79, 3570.75,
            1984.5, 3751.33, 3669.64, 2428.85, 3313.65, 2728.03,
            2523.34, 2908.49, 2428.85, 4445.67, 3669.65, 2632.01,
            2627.48, 4348.79, 3313.65, 3669.65, 4544.92, 3055.37,
            2254.82, 3570.75, 2728.03, 2632.01, 3055.37, 3283.66;

    Eigen::VectorXd x(6);
    x << 11.8978, 9.56156, 5.49005, 5.12391, 8.19604, 8.60379;

    Eigen::VectorXd b(6);
    b << 13.9565, 11.3748, 3.58291, 6.76643, 11.9444, 1.51398;


    Eigen::VectorXd xy = -A.fullPivLu().solve(b);



    std::cout<<"this is matrix A: "<<std::endl;
    std::cout<<A<<std::endl;
    std::cout<<"this is eigenvalue: "<<std::endl<<A.eigenvalues()<<std::endl;
    std::cout<<"this is vector x: "<<std::endl;
    std::cout<<x<<std::endl;
    std::cout<<"this is vector b: "<<std::endl;
    std::cout<<b<<std::endl;
    std::cout<<"this is veccotr(x*) : "<<std::endl<<xy<<std::endl;
    std::cout<<"this is f(x*): "<<f(xy,A,b)<<std::endl;


    int count = 1;
    Eigen::MatrixXd M(dim,dim);
    std::vector<Eigen::VectorXd> list_of_x;

    calculate_gradient(x,A,b,list_of_x,count,M);

    std::cout<<"the sum of iterator: "<<count<<std::endl;
}
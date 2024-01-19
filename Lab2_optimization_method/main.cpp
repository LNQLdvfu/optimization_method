#include <iostream>
#include <vector>
#include <cmath>
#include <Eigen/Dense>
#include <chrono>
#include <random>
using namespace Eigen;
using namespace std;
using vec = Matrix<double, Dynamic, 1>;
using mat = Matrix<double, Dynamic, Dynamic>;

mat gen_matrix( int dim) {
    Eigen::MatrixXd random_matrix(dim,dim) ;
//    std::minstd_rand random (std::chrono::system_clock::now().time_since_epoch().count());
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(1e-10, 1);


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

vec gen_vec(double low = 1e-3, double high = 1, int dim = 4) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(low, high);

    vec v(dim);
    for (int i = 0; i < dim; ++i) {
        v(i) = dis(gen);
    }
    return v;
}

double f_origin(const mat& A, const vec& b, const vec& x) {
    return (x.transpose() / 2 * A * x + b.transpose() * x)(0);
}

vec gen_vec_nearby(const vec& x, int dim = 4) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(-1e+14, 1e+14);

    vec v(dim);
    for (int i = 0; i < dim; ++i) {
        v(i) = dis(gen) + x(i);
    }
    return v;
}

vec f(const mat& A, const vec& b, double r, const vec& x, const vec& x0, double y) {
    int dim = A.rows() + 1;
    vec pre_res = (A + 2 * MatrixXd::Identity(dim-1, dim-1) * y) * x + b + 2 * y * x0;
    vec result(dim);
    result.head(dim-1) = pre_res;
    result(dim-1) = (x - x0).squaredNorm() - r*r;
    return result;
}

mat jacobian(const mat& A, const vec& x, const vec& x0, double y) {
    int dim = A.rows() + 1;
    mat m(dim, dim);
    m.block(0, 0, dim-1, dim-1) = A + 2 * MatrixXd::Identity(dim-1, dim-1) * y;
    m.block(0, dim-1, dim-1, 1) = 2 * (x - x0);
    m.block(dim-1, 0, 1, dim-1) = (2 * (x - x0)).transpose();
    m(dim-1, dim-1) = 0;
    return m;
}

vec newton(const mat& A, const vec& b, double r, const vec& xk, const vec& x0) {
    mat jac = jacobian(A, xk.head(xk.rows()-1), x0, xk(xk.rows()-1));
    return xk - jac.inverse() * f(A, b, r, xk.head(xk.rows()-1), x0, xk(xk.rows()-1));
}

void calc(const mat& A, const vec& b, const vec& x0,const double& r, const vector<vec>& x_approx) {
    double y = r;
    vec xy = -A.fullPivLu().solve(b);
    cout << "y = 0:" << endl;
    cout << "x* = " << xy.transpose() << endl;
    cout << "f(x*) = " << f_origin(A, b, xy) << endl;
    cout << "||x-x0|| ? r:" << endl;
    cout << (xy - x0).norm() << " <= " << r << endl;
    int i{};
    for (const auto& x : x_approx) {
        vec x_prev = x;
        vec xk = newton(A, b, y, x_prev, x0);
        while ((xk - x_prev).norm() > 1e-6) {
            x_prev = xk;
            xk = newton(A, b, r, x_prev, x0);
        }
        cout << "xk: " << xk.transpose() << endl;
        cout<<"x["<<i<<"]"<<x<<endl;
        cout << "f(x): " << f_origin(A, b, xk.head(xk.rows()-1)) << endl;
        i++;
    }
}

int main() {
    int dim = 4;
//    mat A = gen_matrix(dim);
//    vec b = gen_vec();
//    vec x = gen_vec();
//    vec x0 = gen_vec();

    mat A (4,4);
    A << 0.250305, 0.179794, 0.298138, 0.359237,
        0.179794, 0.266553 ,0.338826,  0.62314,
        0.298138, 0.338826, 0.704411, 0.812338,
        0.359237,  0.62314, 0.812338,  1.50021;
    vec b (4);
    b << 0.447025,0.175966,0.870033,0.531168;

    vec x (4);
    x << 0.138974,0.137909,0.235623,0.259103;
    vec x0 (4);

    x0<< 0.931839,0.998959,0.95722,0.338306;

    cout<<"matrix A:"<<endl<<A<<endl;
    cout<<"vecotr b:"<<endl<<b<<endl;
    cout<<"vecotr x:"<<endl<<x<<endl;
    cout<<"vector x0:"<<endl<<x0<<endl;




    const double r = M_PI;

    std::vector<VectorXd> x_approx;
    for (int i = 0; i < 8; ++i) {
        VectorXd x = gen_vec_nearby(x0);
        x.conservativeResize(x.size() + 1);
        x(x.size() - 1) = r;
        x_approx.push_back(x);
    }



    calc(A,b,x0,r,x_approx);

}
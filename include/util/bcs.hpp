
#include "constants.hpp"
#include "input_parser.hpp"
#include <Eigen/Dense>

namespace BCS {
using namespace Eigen;

typedef struct {
  VectorXd u2;
  VectorXd v2;
  VectorXd Delta;
  VectorXd qpEnergies;
  double lambda;
  double Epair;
} BCSResult;

BCSResult BCSiter(const MatrixXcd &phi, const VectorXd &eps, int A,
                  PairingParameters params, NucleonType t,
                  const VectorXd &rho0norm, const VectorXd &oldDelta,
                  double oldLambda);
} // namespace BCS

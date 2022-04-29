public class ThreePrisonersDilemma {

	/*
	 * This Java program models the two-player Prisoner's Dilemma game.
	 * We use the integer "0" to represent cooperation, and "1" to represent
	 * defection.
	 * 
	 * Recall that in the 2-players dilemma, U(DC) > U(CC) > U(DD) > U(CD), where
	 * we give the payoff for the first player in the list. We want the three-player
	 * game
	 * to resemble the 2-player game whenever one player's response is fixed, and we
	 * also want symmetry, so U(CCD) = U(CDC) etc. This gives the unique ordering
	 * 
	 * U(DCC) > U(CCC) > U(DDC) > U(CDC) > U(DDD) > U(CDD)
	 * 
	 * The payoffs for player 1 are given by the following matrix:
	 */

	static int[][][] payoff = {
			{ { 6, 3 }, // payoffs when first and second players cooperate
					{ 3, 0 } }, // payoffs when first player coops, second defects
			{ { 8, 5 }, // payoffs when first player defects, second coops
					{ 5, 2 } } };// payoffs when first and second players defect

	/*
	 * So payoff[i][j][k] represents the payoff to player 1 when the first
	 * player's action is i, the second player's action is j, and the
	 * third player's action is k.
	 * 
	 * In this simulation, triples of players will play each other repeatedly in a
	 * 'match'. A match consists of about 100 rounds, and your score from that match
	 * is the average of the payoffs from each round of that match. For each round,
	 * your
	 * strategy is given a list of the previous plays (so you can remember what your
	 * opponent did) and must compute the next action.
	 */

	abstract class Player {
		// This procedure takes in the number of rounds elapsed so far (n), and
		// the previous plays in the match, and returns the appropriate action.
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			throw new RuntimeException("You need to override the selectAction method.");
		}

		// Used to extract the name of this player class.
		final String name() {
			String result = getClass().getName();
			return result.substring(result.indexOf('$') + 1);
		}
	}

	/* Here are four simple strategies: */

	class NicePlayer extends Player {
		// NicePlayer always cooperates
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			return 0;
		}
	}

	class NastyPlayer extends Player {
		// NastyPlayer always defects
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			return 1;
		}
	}

	class RandomPlayer extends Player {
		// RandomPlayer randomly picks his action each time
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			if (Math.random() < 0.5)
				return 0; // cooperates half the time
			else
				return 1; // defects half the time
		}
	}

	class TolerantPlayer extends Player {
		// TolerantPlayer looks at his opponents' histories, and only defects
		// if at least half of the other players' actions have been defects
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			int opponentCoop = 0;
			int opponentDefect = 0;
			for (int i = 0; i < n; i++) {
				if (oppHistory1[i] == 0)
					opponentCoop = opponentCoop + 1;
				else
					opponentDefect = opponentDefect + 1;
			}
			for (int i = 0; i < n; i++) {
				if (oppHistory2[i] == 0)
					opponentCoop = opponentCoop + 1;
				else
					opponentDefect = opponentDefect + 1;
			}
			if (opponentDefect > opponentCoop)
				return 1;
			else
				return 0;
		}
	}

	class FreakyPlayer extends Player {
		// FreakyPlayer determines, at the start of the match,
		// either to always be nice or always be nasty.
		// Note that this class has a non-trivial constructor.
		int action;

		FreakyPlayer() {
			if (Math.random() < 0.5)
				action = 0; // cooperates half the time
			else
				action = 1; // defects half the time
		}

		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			return action;
		}
	}

	class T4TPlayer extends Player {
		// Picks a random opponent at each play,
		// and uses the 'tit-for-tat' strategy against them
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			if (n == 0)
				return 0; // cooperate by default
			if (Math.random() < 0.5)
				return oppHistory1[n - 1];
			else
				return oppHistory2[n - 1];
		}
	}

	class Javelin_Player extends Player {
        int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {

            // Rule 1: our agent will cooperate in the first round
            if (n == 0)  {
                return 0;
            }

            // Rule 2: our agent will defect in the last few rounds, NastyPlayer mode is turned on
            if (n > 95) {
                return 1;
            }

            // Rule 3: if all players including our agent cooperated in the previous round,
            // then our agent will continue to cooperate
            if (myHistory[n-1] == 0 && oppHistory1[n-1] == 0 && oppHistory2[n-1] == 0) {
                return 0;
            }

            // Rule 4: check opponents history to see if they have defected before
            for (int i = 0; i < n; i++) {
                if (oppHistory1[i] == 1 || oppHistory2[i] == 1) {
                    // if either one of them defected before, our agent will always defect
                    return 1;
                }
            }
            // Rule 5: Otherwise, by default nature, our agent will always cooperate
            return 0;
        }
    }

	class Junyuan_Player extends Player {
		// Helper function to calculate percentage of cooperation
		float calCoopPercentage(int[] history) {
			int cooperates = 0;
			int length = history.length;
	
			for (int i = 0; i < length; i++)
				if (history[i] == 0)
					cooperates++;
	
			return (float) cooperates / length * 100;
		}
	
		int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			if (n == 0)
				return 0; // First round: Cooperate
	
			/* 1. Calculate percentage of cooperation */
			float perOpp1Coop = calCoopPercentage(oppHistory1);
			float perOpp2Coop = calCoopPercentage(oppHistory2);
	
			/* 2. If both players are mostly cooperating */
			if (perOpp1Coop > 90 && perOpp2Coop > 90) {
				int range = (10 - 5) + 1; // Max: 10, Min: 5
				int random = (int) (Math.random() * range) + 5;
				
				if (n > (90 + random))  // Selfish: Last min defect
					return 1;
				else
					return 0;	// First ~90 rounds: Cooperate
			}
	
			/* 3. Defect by default */
			return 1;
		}
	}

	class LIM_KAISHENG_Player extends Player {
		// Helper function for TitForTwoTats
		boolean defected_twice(int[] history) {
			int count = 0;
			int length = history.length;

			if (length < 2)
				return false; 

			for (int i = length - 2; i < length; i++) {
				if (history[i] == 1) {
					count++;
				}
			}

			if (count == 2)
				return true;
			else
				return false;
		}

		// Helper function for SoftMajority
		float cooperate(int[] history) {
			int count = 0;
			int length = history.length;
	
			for (int i = 0; i < length; i++)
				if (history[i] == 0)
					count++;
	
			return (float) count / length;
		}

        int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			/* 1. Cooperate in first round */
			if (n == 0)
				return 0;
			
			/* 2. Closing to the end of the game, defect to maximize rewards.
			Set N to a smaller value assuming most other players will do this trick as well */
			if (n > 90) { 
				return 1; 
			}

			/* Tit-for-twice-tats
			Cross over to defection once both players had defected twice defecting */
			boolean opp1 = defected_twice(oppHistory1);
			boolean opp2 = defected_twice(oppHistory2);

			if (opp1 && opp2) {
				return 1; 
			}

			/* 3. SoftMajority Strategy
			With percentage tuned higher */
			float percentage1 = cooperate(oppHistory1);
			float percentage2 = cooperate(oppHistory2);
			if (percentage1 >= 0.6 && percentage2 >= 0.6){
				return 0; // Cooperate since opponents are cooperative
			}
			else{
				return 1; // Defect since opponents are defecting
			}
		}
    }

	class SoftMajority extends Player {
		// Helper function for SoftMajority
		float cooperate(int[] history) {
			int count = 0;
			int length = history.length;
	
			for (int i = 0; i < length; i++)
				if (history[i] == 0)
					count++;
	
			return (float) count / length;
		}

        int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			/* 1. Cooperate in first round */
			if (n == 0)
				return 0;
			
			/* 2. Closing to the end of the game, defect to maximize rewards.
			Set N to a smaller value assuming most other players will do this trick as well */
			if (n > 90) { 
				return 1; 
			}

			/* 4. SoftMajority Strategy with percentage tuned higher */
			float perOpp1Coop = cooperate(oppHistory1);
			float perOpp2Coop = cooperate(oppHistory2);
			if (perOpp1Coop >= 0.6 && perOpp2Coop >= 0.6){
				return 0; // Cooperate since opponents are cooperative
			}
			else{
				return 1; // Defect since opponents are defecting
			}
		}
    }

	class TitForTwoTats extends Player {
		// Helper function for TitForTwoTats
		boolean defected_twice(int[] history) {
			int count = 0;
			int length = history.length;

			if (length < 2)
				return false; 

			for (int i = length - 2; i < length; i++) {
				if (history[i] == 1) {
					count++;
				}
			}

			if (count == 2)
				return true;
			else
				return false;
		}
		/*Cooperates on the first move, and defects only when the opponent defects two times*/
        int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
			/* Cooperate by default*/
			if (n == 0)
				return 0; // First round: Cooperate

			if (n > 95) {
				return 1;
			}
			boolean opp1 = defected_twice(oppHistory1);
			boolean opp2 = defected_twice(oppHistory2);

			if (opp1 || opp2) {
				return 1; // Defect since opponent defected twice
			}
			else{
				return 0; // Cooperate otherwise
			}
		}
    }

	/*
	 * In our tournament, each pair of strategies will play one match against each
	 * other.
	 * This procedure simulates a single match and returns the scores.
	 */
	float[] scoresOfMatch(Player A, Player B, Player C, int rounds) {
		int[] HistoryA = new int[0], HistoryB = new int[0], HistoryC = new int[0];
		float ScoreA = 0, ScoreB = 0, ScoreC = 0;

		for (int i = 0; i < rounds; i++) {
			int PlayA = A.selectAction(i, HistoryA, HistoryB, HistoryC);
			int PlayB = B.selectAction(i, HistoryB, HistoryC, HistoryA);
			int PlayC = C.selectAction(i, HistoryC, HistoryA, HistoryB);
			ScoreA = ScoreA + payoff[PlayA][PlayB][PlayC];
			ScoreB = ScoreB + payoff[PlayB][PlayC][PlayA];
			ScoreC = ScoreC + payoff[PlayC][PlayA][PlayB];
			HistoryA = extendIntArray(HistoryA, PlayA);
			HistoryB = extendIntArray(HistoryB, PlayB);
			HistoryC = extendIntArray(HistoryC, PlayC);
		}
		float[] result = { ScoreA / rounds, ScoreB / rounds, ScoreC / rounds };
		return result;
	}

	// This is a helper function needed by scoresOfMatch.
	int[] extendIntArray(int[] arr, int next) {
		int[] result = new int[arr.length + 1];
		for (int i = 0; i < arr.length; i++) {
			result[i] = arr[i];
		}
		result[result.length - 1] = next;
		return result;
	}

	/*
	 * The procedure makePlayer is used to reset each of the Players
	 * (strategies) in between matches. When you add your own strategy,
	 * you will need to add a new entry to makePlayer, and change numPlayers.
	 */
	////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////
	int numPlayers = 6 + 3;
	Player makePlayer(int which) {
		switch (which) {
			case 0:
				return new NicePlayer();
			case 1:
				return new NastyPlayer();
			case 2:
				return new RandomPlayer();
			case 3:
				return new TolerantPlayer();
			case 4:
				return new FreakyPlayer();
			case 5:
				return new T4TPlayer();
			case 6:
				return new SoftMajority();
			case 7:
				return new TitForTwoTats();
			case 8:
				return new LIM_KAISHENG_Player();
			case 9:
				return new Javelin_Player();
			case 10:
				return new Junyuan_Player();
		}
		////////////////////////////////////////////////////////////////////////////////////////////////
		////////////////////////////////////////////////////////////////////////////////////////////////
		throw new RuntimeException("Bad argument passed to makePlayer");
	}

	/* Finally, the remaining code actually runs the tournament. */

	public static void main(String[] args) {
		ThreePrisonersDilemma instance = new ThreePrisonersDilemma();
		instance.runTournament();
	}

	boolean verbose = false; // set verbose = false if you get too much text output

	void runTournament() {
		float[] totalScore = new float[numPlayers];

		// This loop plays each triple of players against each other.
		// Note that we include duplicates: two copies of your strategy will play once
		// against each other strategy, and three copies of your strategy will play
		// once.

		for (int looper = 0; looper < 100; looper++){
			// Make all 6 players compete against each other (combination by selection)
			for (int i = 0; i < numPlayers; i++)
				for (int j = i; j < numPlayers; j++)
					for (int k = j; k < numPlayers; k++) {

						Player A = makePlayer(i); // Create a fresh copy of each player
						Player B = makePlayer(j);
						Player C = makePlayer(k);
						int rounds = 90 + (int) Math.rint(20 * Math.random()); // Between 90 and 110 rounds
						float[] matchResults = scoresOfMatch(A, B, C, rounds); // Run match
						// Store the total scores into each player_strategy int array. Total of 6 arrays, bc there's 6 player_strategy.
						totalScore[i] = totalScore[i] + matchResults[0];
						totalScore[j] = totalScore[j] + matchResults[1];
						totalScore[k] = totalScore[k] + matchResults[2];
						if (verbose)
							System.out.println(A.name() + " scored " + matchResults[0] +
									" points, " + B.name() + " scored " + matchResults[1] +
									" points, and " + C.name() + " scored " + matchResults[2] + " points.");
					}
		}

		int[] sortedOrder = new int[numPlayers];
		// This loop sorts the players by their score. (insertion sort)
		for (int i = 0; i < numPlayers; i++) {
			int j = i - 1;
			for (; j >= 0; j--) {
				if (totalScore[i] > totalScore[sortedOrder[j]])
					sortedOrder[j + 1] = sortedOrder[j];
				else
					break;
			}
			sortedOrder[j + 1] = i;
		}

		// Finally, print out the sorted results.
		if (verbose)
			System.out.println();
		System.out.println("Tournament Results");
		for (int i = 0; i < numPlayers; i++)
			System.out.println((i+1) + ". "+ makePlayer(sortedOrder[i]).name() + " : "
					+ totalScore[sortedOrder[i]] + " points.");

	} // end of runTournament()

} // end of class PrisonersDilemma

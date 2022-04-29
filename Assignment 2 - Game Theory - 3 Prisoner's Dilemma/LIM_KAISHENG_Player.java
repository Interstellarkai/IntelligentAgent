/**
 * Assignment 2: Hybrid Tit-For-Twice-Tats + Soft Majority strategy
 * 
 * @author LIM KAI SHENG (U2020321C)
 *
 */
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

		/* 3. Tit-For-Twice-Tats Strategy
		Cross over to defection once both players had defected twice defecting */
		boolean opp1 = defected_twice(oppHistory1);
		boolean opp2 = defected_twice(oppHistory2);

		if (opp1 && opp2) {
			return 1; 
		}

		/* 4. SoftMajority Strategy
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

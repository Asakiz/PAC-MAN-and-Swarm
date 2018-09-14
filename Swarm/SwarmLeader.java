package Swarm;
import robocode.*;
import java.io.IOException;
import static robocode.util.Utils.normalRelativeAngleDegrees;

// API help : http://robocode.sourceforge.net/docs/robocode/robocode/Robot.html

/**
 * BeeLeader - a robot by (your name here)
 */
public class SwarmLeader extends TeamRobot
{
	/**
	 * run: BeeLeader's default behavior
	 */
	public void run() {
		int turn=0;
		while(true) {
			// Anda pelo mapa girando o radar
			ahead(100);
			if(turn==0){
				setTurnRadarRight(10000);
				turnRight(60);
				turn=1;
			}
			else
			{
				setTurnRadarRight(10000);
				turnLeft(60);
				turn=0;
			}
		}
	}

	/**
	 * onScannedRobot: What to do when you see another robot
	 */
	public void onScannedRobot(ScannedRobotEvent e) {
		if(isTeammate(e.getName())){
			//Nao atira
		}
		else {
			double enemyPos=this.getHeading() + e.getBearing();
			double x= getX() + e.getDistance() * Math.sin(Math.toRadians(enemyPos));
			double y= getY() + e.getDistance() * Math.cos(Math.toRadians(enemyPos));
			
			Point enemyPoint= new Point(x, y);
			try{
				broadcastMessage(enemyPoint);
			}
			catch(IOException ex){
				
			}
			seekAndDestroy(enemyPoint);
			
		}
	}
	
	public void seekAndDestroy(Point p){
		double dx = p.getX() - this.getX();
		double dy = p.getY() - this.getY();
		// Calculate angle to target
		double theta = Math.toDegrees(Math.atan2(dx, dy));
		// Turn gun to target
		turnGunRight(normalRelativeAngleDegrees(theta - getGunHeading()));
		// Fire hard!
		fire(3);
	}

	/**
	 * onHitByBullet: What to do when you're hit by a bullet
	 */
	public void onHitByBullet(HitByBulletEvent e) {
		turnLeft(45);
		
		ahead(100);
	}
	
	/**
	 * onHitWall: What to do when you hit a wall
	 */
	public void onHitWall(HitWallEvent e) {
		turnRight(180);
		ahead(20);
	}	
	
	public void OnHitRobot(HitRobotEvent evnt)
	{
	    if (evnt.getBearing() > -90 && evnt.getBearing() <= 90)
	    {
	        back(100);
			turnRight(90);
			ahead(100);
	    }
	    else
	    {
	        ahead(100);
	    }
	}
}

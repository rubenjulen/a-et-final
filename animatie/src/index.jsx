import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip } from './Clip';
import { ClipFull } from './ClipFull';
import timingFull from './timing_full.json';
import { Clip3 } from './Clip3';
import timingC3 from './timing_c3.json';
import { Clip4 } from './Clip4';
import timingC4 from './timing_c4.json';
import timing from './timing.json';

const FPS = 30;

const Root = () => (
  <Composition
    id="Clip2Proef"
    component={Clip}
    durationInFrames={Math.ceil(timing.total * FPS)}
    fps={FPS}
    width={1920}
    height={1080}
  />
);
const RootAll = () => (<>
  <Root />
  <Composition id="Clip2Full" component={ClipFull} durationInFrames={Math.ceil(timingFull.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip3" component={Clip3} durationInFrames={Math.ceil(timingC3.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip4" component={Clip4} durationInFrames={Math.ceil(timingC4.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);

registerRoot(RootAll);
